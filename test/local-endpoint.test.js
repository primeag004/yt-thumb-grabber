import assert from 'node:assert/strict';
import test from 'node:test';
import { apiUrl, defaultEndpoint, localEndpoint } from '../lib/local-endpoint.js';

test('accepts loopback HTTP endpoints only', () => {
  assert.equal(localEndpoint('http://127.0.0.1:11434')?.href, 'http://127.0.0.1:11434/');
  assert.equal(localEndpoint('http://localhost:8080/v1')?.href, 'http://localhost:8080/v1');
  assert.equal(localEndpoint('https://example.com'), null);
  assert.equal(localEndpoint('http://192.168.1.20:8080'), null);
  assert.equal(localEndpoint('not an address'), null);
});

test('removes credentials and fragments from an accepted endpoint', () => {
  const endpoint = localEndpoint('http://user:secret@localhost:8080/v1#ignore');
  assert.equal(endpoint?.href, 'http://localhost:8080/v1');
});

test('joins model API routes without losing an OpenAI-compatible API prefix', () => {
  assert.equal(apiUrl('http://127.0.0.1:8080/v1', 'chat/completions').href, 'http://127.0.0.1:8080/v1/chat/completions');
  assert.equal(apiUrl('http://127.0.0.1:11434/', '/api/tags').href, 'http://127.0.0.1:11434/api/tags');
});

test('uses useful provider defaults', () => {
  assert.equal(defaultEndpoint('ollama'), 'http://127.0.0.1:11434');
  assert.equal(defaultEndpoint('openai'), 'http://127.0.0.1:8080/v1');
});
