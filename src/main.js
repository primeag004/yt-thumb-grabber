import { extractVideoId, thumbnailUrl } from './youtube.js';

const $ = (selector) => document.querySelector(selector);
const form = $('#grabber-form');
const input = $('#video-url');
const message = $('#form-message');
const result = $('#result');
const preview = $('#thumbnail-preview');
const qualityBadge = $('#quality-badge');
const qualityButtons = [...document.querySelectorAll('[data-quality]')];
let currentId = '';
let currentQuality = 'maxresdefault';

const qualityLabels = { maxresdefault: 'MAX · 1280 × 720', sddefault: 'SD · 640 × 480', hqdefault: 'HQ · 480 × 360' };
const showToast = (text) => {
  const toast = $('#toast');
  toast.textContent = text;
  toast.classList.add('show');
  clearTimeout(showToast.timer);
  showToast.timer = setTimeout(() => toast.classList.remove('show'), 2400);
};

function setPreview(quality) {
  currentQuality = quality;
  preview.classList.add('loading');
  preview.src = thumbnailUrl(currentId, quality);
  qualityBadge.textContent = qualityLabels[quality];
  qualityButtons.forEach((button) => button.classList.toggle('active', button.dataset.quality === quality));
}

preview.addEventListener('load', () => preview.classList.remove('loading'));
preview.addEventListener('error', () => {
  if (currentQuality === 'maxresdefault') {
    setPreview('hqdefault');
    showToast('Max resolution unavailable — showing high quality.');
  }
});

form.addEventListener('submit', (event) => {
  event.preventDefault();
  const id = extractVideoId(input.value);
  if (!id) {
    form.classList.add('invalid');
    message.textContent = 'Please enter a valid YouTube video link.';
    input.focus();
    return;
  }
  form.classList.remove('invalid');
  message.textContent = 'Found it — choose a quality and download your thumbnail.';
  currentId = id;
  result.hidden = false;
  setPreview('maxresdefault');
  result.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
});

input.addEventListener('input', () => {
  form.classList.remove('invalid');
  $('#clear-button').classList.toggle('visible', input.value.length > 0);
});
$('#clear-button').addEventListener('click', () => { input.value = ''; input.focus(); $('#clear-button').classList.remove('visible'); });
qualityButtons.forEach((button) => button.addEventListener('click', () => setPreview(button.dataset.quality)));

$('#download-button').addEventListener('click', async () => {
  const url = thumbnailUrl(currentId, currentQuality);
  try {
    const response = await fetch(url);
    if (!response.ok) throw new Error('Image unavailable');
    const blobUrl = URL.createObjectURL(await response.blob());
    const anchor = document.createElement('a');
    anchor.href = blobUrl;
    anchor.download = `youtube-thumbnail-${currentId}-${currentQuality}.jpg`;
    anchor.click();
    setTimeout(() => URL.revokeObjectURL(blobUrl), 1000);
    showToast('Download started.');
  } catch {
    window.open(url, '_blank', 'noopener,noreferrer');
    showToast('Image opened in a new tab.');
  }
});

$('#copy-button').addEventListener('click', async () => {
  try { await navigator.clipboard.writeText(thumbnailUrl(currentId, currentQuality)); showToast('Thumbnail URL copied.'); }
  catch { showToast('Could not copy — please try again.'); }
});

const root = document.documentElement;
const savedTheme = localStorage.getItem('thumbcatch-theme');
const initialTheme = savedTheme || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
root.dataset.theme = initialTheme;
$('#theme-toggle').addEventListener('click', () => {
  root.dataset.theme = root.dataset.theme === 'dark' ? 'light' : 'dark';
  localStorage.setItem('thumbcatch-theme', root.dataset.theme);
  $('#theme-toggle').setAttribute('aria-label', `Switch to ${root.dataset.theme === 'dark' ? 'light' : 'dark'} theme`);
});
document.querySelectorAll('details').forEach((detail) => detail.addEventListener('toggle', () => {
  if (detail.open) document.querySelectorAll('details').forEach((other) => { if (other !== detail) other.open = false; });
}));
$('#year').textContent = new Date().getFullYear();
