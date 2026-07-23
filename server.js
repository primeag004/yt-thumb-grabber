import { createReadStream, existsSync, promises as fs } from 'node:fs';
import { createServer } from 'node:http';
import { extname, join, normalize, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { apiUrl, localEndpoint } from './lib/local-endpoint.js';

const root = fileURLToPath(new URL('.', import.meta.url));
const host = process.env.HOST || '127.0.0.1';
const port = Number(process.env.PORT || 12076);
const MAX_BODY_BYTES = 1_050_000;
const MIME = { '.css': 'text/css; charset=utf-8', '.html': 'text/html; charset=utf-8', '.js': 'application/javascript; charset=utf-8', '.json': 'application/json; charset=utf-8', '.svg': 'image/svg+xml' };

function sendJson(response, status, body) {
  response.writeHead(status, { 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'no-store' });
  response.end(JSON.stringify(body));
}

async function readJson(request) {
  const chunks = [];
  let size = 0;
  for await (const chunk of request) {
    size += chunk.length;
    if (size > MAX_BODY_BYTES) throw new Error('Request is too large.');
    chunks.push(chunk);
  }
  try { return JSON.parse(Buffer.concat(chunks).toString('utf8')); }
  catch { throw new Error('Request body must be valid JSON.'); }
}

function endpointFrom(payload) {
  const endpoint = localEndpoint(payload.endpoint);
  if (!endpoint) throw new Error('Only localhost / loopback model endpoints are allowed.');
  if (!['ollama', 'openai'].includes(payload.provider)) throw new Error('Unknown model provider.');
  return endpoint;
}

function modelRequest(payload) {
  const model = String(payload.model || '').trim();
  if (!model) throw new Error('Choose a local model first.');
  const messages = Array.isArray(payload.messages) ? payload.messages
    .filter((message) => ['system', 'user', 'assistant'].includes(message?.role) && typeof message?.content === 'string')
    .map((message) => ({ role: message.role, content: message.content.slice(0, 16000) })) : [];
  if (!messages.length) throw new Error('Send a message to start the conversation.');
  const temperature = Math.max(0, Math.min(1.5, Number(payload.temperature) || 0.7));
  const maxTokens = Math.max(64, Math.min(4096, Number(payload.maxTokens) || 384));
  return { model, messages, temperature, maxTokens };
}

async function proxyModels(request, response) {
  let payload;
  try { payload = await readJson(request); } catch (error) { sendJson(response, 400, { error: error.message }); return; }
  try {
    const endpoint = endpointFrom(payload);
    const target = apiUrl(endpoint, payload.provider === 'ollama' ? 'api/tags' : 'models');
    const upstream = await fetch(target, { signal: AbortSignal.timeout(8000) });
    const data = await upstream.json().catch(() => ({}));
    if (!upstream.ok) throw new Error(data.error?.message || data.error || `Server returned ${upstream.status}.`);
    const models = payload.provider === 'ollama'
      ? (data.models || []).map((item) => item.name).filter(Boolean)
      : (data.data || []).map((item) => item.id).filter(Boolean);
    sendJson(response, 200, { models });
  } catch (error) {
    sendJson(response, 502, { error: error.message === 'fetch failed' ? 'Could not reach that local model server.' : error.message });
  }
}

async function proxyChat(request, response) {
  let payload;
  try { payload = await readJson(request); } catch (error) { sendJson(response, 400, { error: error.message }); return; }
  const streamController = new AbortController();
  let clientDisconnected = false;
  const stopUpstream = () => { clientDisconnected = true; streamController.abort(); };
  request.once('aborted', stopUpstream);
  response.once('close', stopUpstream);
  const safetyTimeout = setTimeout(stopUpstream, 10 * 60 * 1000);
  try {
    const endpoint = endpointFrom(payload);
    const { model, messages, temperature, maxTokens } = modelRequest(payload);
    const isOllama = payload.provider === 'ollama';
    const target = apiUrl(endpoint, isOllama ? 'api/chat' : 'chat/completions');
    const body = isOllama
      ? { model, messages, stream: true, options: { temperature, num_predict: maxTokens } }
      : { model, messages, stream: true, temperature, max_tokens: maxTokens };
    const upstream = await fetch(target, { method: 'POST', headers: { 'Content-Type': 'application/json', Accept: isOllama ? 'application/x-ndjson' : 'text/event-stream' }, body: JSON.stringify(body), signal: streamController.signal });
    if (!upstream.ok || !upstream.body) {
      const data = await upstream.json().catch(() => ({}));
      throw new Error(data.error?.message || data.error || `Model server returned ${upstream.status}.`);
    }
    response.writeHead(200, { 'Content-Type': upstream.headers.get('content-type') || (isOllama ? 'application/x-ndjson' : 'text/event-stream'), 'Cache-Control': 'no-store', Connection: 'keep-alive' });
    const reader = upstream.body.getReader();
    try {
      while (!clientDisconnected) {
        const { done, value } = await reader.read();
        if (done) break;
        if (!response.write(Buffer.from(value))) await new Promise((resolveDrain) => { response.once('drain', resolveDrain); response.once('close', resolveDrain); });
      }
    } finally { if (!response.destroyed) response.end(); }
  } catch (error) {
    if (clientDisconnected) return;
    if (!response.headersSent) sendJson(response, 502, { error: error.message === 'fetch failed' ? 'Could not reach that local model server.' : error.message });
    else if (!response.destroyed) response.end();
  } finally {
    clearTimeout(safetyTimeout);
  }
}

async function serveFile(request, response, pathname) {
  const requested = pathname === '/' ? '/index.html' : pathname;
  const filePath = resolve(root, `.${normalize(requested)}`);
  if (!filePath.startsWith(root) || !existsSync(filePath)) { sendJson(response, 404, { error: 'Not found.' }); return; }
  try {
    const stats = await fs.stat(filePath);
    if (!stats.isFile()) { sendJson(response, 404, { error: 'Not found.' }); return; }
    response.writeHead(200, { 'Content-Type': MIME[extname(filePath)] || 'application/octet-stream', 'Cache-Control': requested.startsWith('/src/') ? 'no-cache' : 'no-store', 'X-Content-Type-Options': 'nosniff' });
    createReadStream(filePath).pipe(response);
  } catch { sendJson(response, 500, { error: 'Could not load this file.' }); }
}

const server = createServer(async (request, response) => {
  const url = new URL(request.url || '/', `http://${request.headers.host || host}`);
  if (request.method === 'POST' && url.pathname === '/api/models') return proxyModels(request, response);
  if (request.method === 'POST' && url.pathname === '/api/chat') return proxyChat(request, response);
  if (request.method === 'GET' || request.method === 'HEAD') return serveFile(request, response, url.pathname);
  sendJson(response, 405, { error: 'Method not allowed.' });
});

server.listen(port, host, () => console.log(`\n  Niji Local is ready at http://${host}:${port}\n  Press Ctrl+C to stop it.\n`));
