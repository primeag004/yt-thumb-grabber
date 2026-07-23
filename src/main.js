const STORAGE_KEY = 'niji-local.workspace.v1';
const SETTINGS_DEFAULTS = {
  provider: 'ollama',
  endpoint: 'http://127.0.0.1:11434',
  model: '',
  temperature: 0.7,
  maxTokens: 384,
  ecoMode: true,
  systemPrompt: 'You are a thoughtful, helpful assistant. Be direct, honest, and useful.'
};

const icons = {
  plus: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg>',
  close: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m6 6 12 12M18 6 6 18"/></svg>',
  menu: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>',
  sun: '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="3.5"/><path d="M12 2.5v2M12 19.5v2M5.28 5.28l1.42 1.42m10.6 10.6 1.42 1.42M2.5 12h2m15 0h2M5.28 18.72l1.42-1.42m10.6-10.6 1.42-1.42"/></svg>',
  moon: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20.2 15.6A8.5 8.5 0 0 1 8.4 3.8 8.7 8.7 0 1 0 20.2 15.6Z"/></svg>',
  sliders: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 7h7m4 0h5M4 17h3m4 0h9M11 4v6m-4 4v6m8-6v6"/></svg>',
  more: '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="5" cy="12" r="1"/><circle cx="12" cy="12" r="1"/><circle cx="19" cy="12" r="1"/></svg>',
  edit: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m4 20 4.2-1 9.9-9.9a2.1 2.1 0 0 0-3-3L5.2 16 4 20Z"/><path d="m13.8 7.3 3 3"/></svg>',
  trash: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 7h16m-10 4v5m4-5v5M9 7l1-3h4l1 3m-9 0 1 13h10l1-13"/></svg>',
  'arrow-up': '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m12 19V5m0 0-5 5m5-5 5 5"/></svg>',
  stop: '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="7" y="7" width="10" height="10" rx="1"/></svg>',
  copy: '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="8" y="8" width="11" height="12" rx="2"/><path d="M16 8V6a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h2"/></svg>',
  retry: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 11a8 8 0 1 0 1 5.2M20 5v6h-6"/></svg>',
  download: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3v12m0 0 4-4m-4 4-4-4M5 21h14"/></svg>',
  upload: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21V9m0 0-4 4m4-4 4 4M5 3h14"/></svg>',
  plug: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 7V3m6 4V3m-8 8h10v2a5 5 0 0 1-10 0v-2Zm5 7v3"/></svg>'
};

document.querySelectorAll('[data-icon]').forEach((node) => { node.insertAdjacentHTML('afterbegin', icons[node.dataset.icon] || ''); });
const $ = (selector) => document.querySelector(selector);
const ids = () => crypto.randomUUID?.() || `${Date.now()}-${Math.random().toString(16).slice(2)}`;
const now = () => new Date().toISOString();
const newChat = () => ({ id: ids(), title: 'New conversation', createdAt: now(), updatedAt: now(), messages: [] });

function loadWorkspace() {
  try {
    const saved = JSON.parse(localStorage.getItem(STORAGE_KEY) || 'null');
    if (saved && Array.isArray(saved.chats)) {
      const chats = saved.chats.filter((chat) => chat && Array.isArray(chat.messages)).slice(0, 100);
      return { chats: chats.length ? chats : [newChat()], activeChatId: saved.activeChatId, settings: { ...SETTINGS_DEFAULTS, ...saved.settings }, theme: saved.theme || 'dark' };
    }
  } catch { /* Start fresh if an old backup is malformed. */ }
  return { chats: [newChat()], activeChatId: null, settings: { ...SETTINGS_DEFAULTS }, theme: 'dark' };
}

let state = loadWorkspace();
if (!state.chats.some((chat) => chat.id === state.activeChatId)) state.activeChatId = state.chats[0].id;
let isGenerating = false;
let abortController = null;
let toastTimer;

const sidebar = $('#sidebar');
const scrim = $('#scrim');
const chatList = $('#chat-list');
const messageList = $('#message-list');
const emptyState = $('#empty-state');
const messageInput = $('#message-input');
const composer = $('#composer');
const sendButton = $('#send-button');
const stopButton = $('#stop-button');
const settingsDialog = $('#settings-dialog');
const settingsForm = $('#settings-form');
const endpointInput = $('#endpoint-input');
const modelInput = $('#model-input');
const modelOptions = $('#model-options');
const temperatureInput = $('#temperature-input');
const tokensInput = $('#tokens-input');
const ecoInput = $('#eco-input');
const systemPromptInput = $('#system-prompt-input');

function persist() {
  try { localStorage.setItem(STORAGE_KEY, JSON.stringify(state)); }
  catch { showToast('Browser storage is full. Export chats and clear some space.'); }
}
function activeChat() { return state.chats.find((chat) => chat.id === state.activeChatId) || state.chats[0]; }
function shortDate(iso) {
  const date = new Date(iso);
  const today = new Date();
  return date.toDateString() === today.toDateString() ? date.toLocaleTimeString([], { hour: 'numeric', minute: '2-digit' }) : date.toLocaleDateString([], { month: 'short', day: 'numeric' });
}
function defaultEndpoint(provider) { return provider === 'openai' ? 'http://127.0.0.1:8080/v1' : 'http://127.0.0.1:11434'; }
function titleFor(text) { return text.replace(/\s+/g, ' ').trim().slice(0, 42) || 'New conversation'; }
function showToast(text) {
  const toast = $('#toast');
  toast.textContent = text;
  toast.classList.add('show');
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => toast.classList.remove('show'), 3100);
}
function setTheme(theme) {
  state.theme = theme;
  document.documentElement.dataset.theme = theme;
  $('#theme-toggle').dataset.icon = theme === 'dark' ? 'sun' : 'moon';
  $('#theme-toggle').innerHTML = `${icons[$('#theme-toggle').dataset.icon]}<span>Theme</span>`;
  $('meta[name="theme-color"]').content = theme === 'dark' ? '#101411' : '#f5f7f2';
  persist();
}

function renderSidebar() {
  const chat = activeChat();
  chatList.innerHTML = '';
  [...state.chats].sort((a, b) => new Date(b.updatedAt) - new Date(a.updatedAt)).forEach((item) => {
    const button = document.createElement('button');
    button.type = 'button';
    button.className = `chat-item${item.id === chat.id ? ' active' : ''}`;
    button.dataset.chatId = item.id;
    const title = document.createElement('span'); title.textContent = item.title || 'New conversation';
    const time = document.createElement('small'); time.textContent = shortDate(item.updatedAt);
    button.append(title, time);
    chatList.append(button);
  });
}
function messageNode(message, index) {
  const article = document.createElement('article');
  article.className = `message ${message.role}`;
  article.dataset.messageId = message.id;
  const avatar = document.createElement('div');
  avatar.className = 'avatar';
  avatar.textContent = message.role === 'user' ? 'You' : 'N';
  const body = document.createElement('div'); body.className = 'message-body';
  const meta = document.createElement('div'); meta.className = 'message-meta';
  const name = document.createElement('strong'); name.textContent = message.role === 'user' ? 'You' : 'Niji';
  const time = document.createElement('span'); time.textContent = shortDate(message.createdAt);
  meta.append(name, time);
  const content = document.createElement('div'); content.className = 'message-content'; content.textContent = message.content;
  body.append(meta, content);
  if (message.role === 'assistant' && message.content) {
    const actions = document.createElement('div'); actions.className = 'message-actions';
    const copy = document.createElement('button'); copy.type = 'button'; copy.dataset.action = 'copy'; copy.dataset.messageId = message.id; copy.title = 'Copy response'; copy.setAttribute('aria-label', 'Copy response'); copy.innerHTML = icons.copy;
    actions.append(copy);
    if (index === activeChat().messages.length - 1 && !isGenerating) {
      const retry = document.createElement('button'); retry.type = 'button'; retry.dataset.action = 'retry'; retry.title = 'Regenerate response'; retry.setAttribute('aria-label', 'Regenerate response'); retry.innerHTML = icons.retry; actions.append(retry);
    }
    body.append(actions);
  }
  article.append(avatar, body);
  return article;
}
function renderConversation(scroll = false) {
  const chat = activeChat();
  $('#chat-title').textContent = chat.title;
  $('#chat-kicker').textContent = chat.messages.length ? `${chat.messages.length} local message${chat.messages.length === 1 ? '' : 's'}` : 'Private workspace';
  emptyState.hidden = chat.messages.length > 0;
  messageList.innerHTML = '';
  chat.messages.forEach((message, index) => messageList.append(messageNode(message, index)));
  if (scroll) scrollToBottom();
}
function renderAll(scroll = false) { renderSidebar(); renderConversation(scroll); updateModelUI(); }
function scrollToBottom() { requestAnimationFrame(() => { const area = $('#conversation'); area.scrollTop = area.scrollHeight; }); }
function updateMessage(message) {
  const node = messageList.querySelector(`[data-message-id="${CSS.escape(message.id)}"] .message-content`);
  if (node) node.textContent = message.content;
  scrollToBottom();
}
function updateModelUI() {
  const { model, ecoMode } = state.settings;
  $('#model-name').textContent = model || 'Choose a local model';
  $('#eco-chip').hidden = !ecoMode;
  const ready = Boolean(model);
  $('#connection-status').classList.toggle('ready', ready);
  $('#connection-status span').textContent = ready ? 'Local model ready' : 'Model not selected';
  $('#connection-status').title = ready ? `${model} on ${state.settings.endpoint}` : 'Choose a model in settings';
}
function autoSize() {
  messageInput.style.height = 'auto';
  messageInput.style.height = `${Math.min(messageInput.scrollHeight, 180)}px`;
  sendButton.disabled = !messageInput.value.trim() || isGenerating;
}
function showSidebar(open) {
  sidebar.classList.toggle('open', open);
  scrim.hidden = !open;
  document.body.classList.toggle('no-scroll', open);
}

function addChat() {
  if (isGenerating) return;
  const chat = newChat();
  state.chats.unshift(chat);
  state.activeChatId = chat.id;
  persist(); renderAll(); messageInput.focus(); showSidebar(false);
}
function selectChat(id) {
  if (isGenerating || !state.chats.some((chat) => chat.id === id)) return;
  state.activeChatId = id; persist(); renderAll(); showSidebar(false);
}
function deleteChat() {
  if (isGenerating) return;
  const chat = activeChat();
  if (!confirm(`Delete “${chat.title}”? This cannot be undone.`)) return;
  state.chats = state.chats.filter((item) => item.id !== chat.id);
  if (!state.chats.length) state.chats.push(newChat());
  state.activeChatId = state.chats[0].id;
  persist(); renderAll(); $('#conversation-menu').hidden = true; showToast('Conversation deleted.');
}
function renameChat() {
  const chat = activeChat();
  const title = prompt('Name this conversation', chat.title);
  if (title?.trim()) { chat.title = title.trim().slice(0, 80); chat.updatedAt = now(); persist(); renderAll(); }
  $('#conversation-menu').hidden = true;
}

function fillSettings() {
  const settings = state.settings;
  const radio = settingsForm.querySelector(`[name="provider"][value="${settings.provider}"]`);
  if (radio) radio.checked = true;
  endpointInput.value = settings.endpoint;
  modelInput.value = settings.model;
  temperatureInput.value = settings.temperature;
  tokensInput.value = settings.maxTokens;
  ecoInput.checked = settings.ecoMode;
  systemPromptInput.value = settings.systemPrompt;
  updateControlLabels();
  $('#endpoint-help').textContent = settings.provider === 'ollama' ? 'Ollama default: http://127.0.0.1:11434' : 'Include the API path, e.g. http://127.0.0.1:8080/v1';
  $('#connection-feedback').textContent = '';
}
function openSettings() { if (isGenerating) return showToast('Stop the current reply before changing servers.'); fillSettings(); settingsDialog.showModal(); }
function updateControlLabels() { $('#temperature-value').textContent = Number(temperatureInput.value).toFixed(1); $('#tokens-value').textContent = tokensInput.value; }
function settingsPayload() { return { provider: settingsForm.elements.provider.value, endpoint: endpointInput.value.trim(), model: modelInput.value.trim() }; }
function saveSettings() {
  const settings = settingsPayload();
  if (!settings.endpoint || !settings.model) { showToast('Enter both a local server address and model name.'); return false; }
  state.settings = { ...state.settings, ...settings, temperature: Number(temperatureInput.value), maxTokens: Number(tokensInput.value), ecoMode: ecoInput.checked, systemPrompt: systemPromptInput.value.trim() };
  if (state.settings.ecoMode) state.settings.maxTokens = Math.min(384, state.settings.maxTokens);
  persist(); updateModelUI(); return true;
}
async function api(path, payload, signal) {
  const response = await fetch(path, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload), signal });
  if (!response.ok) {
    const error = await response.json().catch(() => ({}));
    throw new Error(error.error || 'The local server returned an error.');
  }
  return response;
}
async function loadModels(showSuccess = true) {
  const feedback = $('#connection-feedback');
  feedback.textContent = 'Looking for local models…';
  try {
    const response = await api('/api/models', settingsPayload());
    const data = await response.json();
    modelOptions.innerHTML = '';
    data.models.forEach((name) => { const option = document.createElement('option'); option.value = name; modelOptions.append(option); });
    if (data.models.length && !data.models.includes(modelInput.value)) modelInput.value = data.models[0];
    feedback.textContent = data.models.length ? `${data.models.length} model${data.models.length === 1 ? '' : 's'} found on this device.` : 'Connected, but no downloaded models were found.';
    if (showSuccess) showToast(data.models.length ? 'Local models loaded.' : 'Server connected — no models found.');
    return data.models;
  } catch (error) { feedback.textContent = error.message; if (showSuccess) showToast(error.message); return []; }
}

function requestMessages(chat) {
  const messages = [];
  if (state.settings.systemPrompt) messages.push({ role: 'system', content: state.settings.systemPrompt });
  chat.messages.filter((message) => message.content.trim()).forEach(({ role, content }) => messages.push({ role, content }));
  return messages;
}
async function consumeStream(response, provider, onText) {
  const reader = response.body?.getReader();
  if (!reader) throw new Error('Your browser could not read the model response.');
  const decoder = new TextDecoder();
  let buffer = '';
  let ended = false;
  while (!ended) {
    const { value, done } = await reader.read();
    buffer += decoder.decode(value || new Uint8Array(), { stream: !done });
    const lines = buffer.split(/\r?\n/);
    buffer = lines.pop() || '';
    for (const rawLine of lines) {
      const line = rawLine.trim();
      if (!line) continue;
      const jsonText = provider === 'openai' ? (line.startsWith('data:') ? line.slice(5).trim() : '') : line;
      if (!jsonText) continue;
      if (jsonText === '[DONE]') { ended = true; break; }
      try {
        const data = JSON.parse(jsonText);
        const piece = provider === 'ollama' ? data.message?.content : data.choices?.[0]?.delta?.content;
        if (piece) onText(piece);
        if (data.done) ended = true;
        if (data.error) throw new Error(typeof data.error === 'string' ? data.error : data.error.message);
      } catch (error) {
        if (error instanceof SyntaxError) continue;
        throw error;
      }
    }
    if (done) break;
  }
}
async function sendMessage(overrideText = null) {
  const content = (overrideText ?? messageInput.value).trim();
  if (!content || isGenerating) return;
  if (!state.settings.model) { openSettings(); showToast('Choose a local model before sending.'); return; }
  const chat = activeChat();
  const userMessage = { id: ids(), role: 'user', content, createdAt: now() };
  chat.messages.push(userMessage);
  if (chat.title === 'New conversation') chat.title = titleFor(content);
  chat.updatedAt = now();
  messageInput.value = ''; autoSize();
  isGenerating = true; abortController = new AbortController();
  stopButton.hidden = false; sendButton.hidden = true;
  persist(); renderAll(true);
  const reply = { id: ids(), role: 'assistant', content: '', createdAt: now() };
  chat.messages.push(reply);
  renderConversation(true);
  try {
    const maxTokens = state.settings.ecoMode ? Math.min(384, state.settings.maxTokens) : state.settings.maxTokens;
    const response = await api('/api/chat', { ...state.settings, maxTokens, messages: requestMessages(chat) }, abortController.signal);
    await consumeStream(response, state.settings.provider, (piece) => { reply.content += piece; updateMessage(reply); });
    if (!reply.content.trim()) throw new Error('The model finished without a response. Check its server logs and model format.');
    chat.updatedAt = now();
  } catch (error) {
    if (error.name === 'AbortError') {
      if (!reply.content) chat.messages.pop();
      showToast('Generation stopped.');
    } else {
      if (!reply.content) chat.messages.pop();
      showToast(error.message || 'Could not reach your local model.');
    }
  } finally {
    isGenerating = false; abortController = null; stopButton.hidden = true; sendButton.hidden = false;
    chat.updatedAt = now(); persist(); renderAll(true); autoSize();
  }
}
function regenerate() {
  const chat = activeChat();
  if (isGenerating || chat.messages.at(-1)?.role !== 'assistant') return;
  chat.messages.pop();
  const previous = chat.messages.at(-1);
  if (previous?.role === 'user') { chat.messages.pop(); sendMessage(previous.content); }
}

$('#new-chat').addEventListener('click', addChat);
$('#open-sidebar').addEventListener('click', () => showSidebar(true));
$('#close-sidebar').addEventListener('click', () => showSidebar(false));
scrim.addEventListener('click', () => showSidebar(false));
chatList.addEventListener('click', (event) => { const button = event.target.closest('[data-chat-id]'); if (button) selectChat(button.dataset.chatId); });
$('#open-settings').addEventListener('click', openSettings);
$('#quick-model').addEventListener('click', openSettings);
$('#theme-toggle').addEventListener('click', () => setTheme(state.theme === 'dark' ? 'light' : 'dark'));
$('#more-button').addEventListener('click', () => { $('#conversation-menu').hidden = !$('#conversation-menu').hidden; });
$('#rename-chat').addEventListener('click', renameChat);
$('#delete-chat').addEventListener('click', deleteChat);
document.addEventListener('click', (event) => { if (!event.target.closest('.topbar-actions')) $('#conversation-menu').hidden = true; });
messageList.addEventListener('click', async (event) => {
  const button = event.target.closest('[data-action]'); if (!button) return;
  if (button.dataset.action === 'copy') {
    const message = activeChat().messages.find((item) => item.id === button.dataset.messageId);
    try { await navigator.clipboard.writeText(message?.content || ''); showToast('Response copied.'); } catch { showToast('Copy failed — select the text manually.'); }
  }
  if (button.dataset.action === 'retry') regenerate();
});
composer.addEventListener('submit', (event) => { event.preventDefault(); sendMessage(); });
messageInput.addEventListener('input', autoSize);
messageInput.addEventListener('keydown', (event) => { if (event.key === 'Enter' && !event.shiftKey && !event.isComposing) { event.preventDefault(); sendMessage(); } });
stopButton.addEventListener('click', () => abortController?.abort());
document.querySelectorAll('[data-prompt]').forEach((button) => button.addEventListener('click', () => { messageInput.value = button.dataset.prompt; autoSize(); messageInput.focus(); }));
document.addEventListener('keydown', (event) => { if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === 'k') { event.preventDefault(); addChat(); } });

settingsForm.addEventListener('change', (event) => {
  if (event.target.name === 'provider') {
    endpointInput.value = defaultEndpoint(event.target.value);
    $('#endpoint-help').textContent = event.target.value === 'ollama' ? 'Ollama default: http://127.0.0.1:11434' : 'Include the API path, e.g. http://127.0.0.1:8080/v1';
  }
});
temperatureInput.addEventListener('input', updateControlLabels);
tokensInput.addEventListener('input', updateControlLabels);
ecoInput.addEventListener('change', () => { if (ecoInput.checked && Number(tokensInput.value) > 384) { tokensInput.value = 384; updateControlLabels(); } });
$('#load-models').addEventListener('click', () => loadModels());
$('#test-connection').addEventListener('click', async () => { const models = await loadModels(false); if (models.length) showToast('Connection is working locally.'); });
settingsForm.addEventListener('submit', (event) => { event.preventDefault(); if (event.submitter?.value === 'save' && saveSettings()) { settingsDialog.close('save'); showToast('Local model settings saved.'); } else if (event.submitter?.value !== 'save') settingsDialog.close('cancel'); });
$('#export-data').addEventListener('click', () => {
  const blob = new Blob([JSON.stringify({ exportedAt: now(), ...state }, null, 2)], { type: 'application/json' });
  const url = URL.createObjectURL(blob); const link = document.createElement('a'); link.href = url; link.download = `niji-local-backup-${new Date().toISOString().slice(0, 10)}.json`; link.click(); URL.revokeObjectURL(url); showToast('Backup downloaded.');
});
$('#import-data').addEventListener('change', async (event) => {
  const file = event.target.files?.[0]; if (!file) return;
  try {
    const imported = JSON.parse(await file.text());
    if (!Array.isArray(imported.chats)) throw new Error('That is not a Niji Local backup.');
    state = { chats: imported.chats.filter((chat) => chat && Array.isArray(chat.messages)).slice(0, 100), activeChatId: imported.activeChatId, settings: { ...SETTINGS_DEFAULTS, ...imported.settings }, theme: imported.theme === 'light' ? 'light' : 'dark' };
    if (!state.chats.length) state.chats = [newChat()];
    if (!state.chats.some((chat) => chat.id === state.activeChatId)) state.activeChatId = state.chats[0].id;
    persist(); setTheme(state.theme); renderAll(); showToast('Backup imported locally.');
  } catch (error) { showToast(error.message || 'Could not import that backup.'); }
  event.target.value = '';
});
$('#clear-data').addEventListener('click', () => {
  if (!confirm('Erase every saved conversation and setting from this browser?')) return;
  state = { chats: [newChat()], activeChatId: null, settings: { ...SETTINGS_DEFAULTS }, theme: state.theme };
  state.activeChatId = state.chats[0].id; persist(); fillSettings(); renderAll(); showToast('Local data cleared.');
});

setTheme(state.theme);
renderAll();
autoSize();
