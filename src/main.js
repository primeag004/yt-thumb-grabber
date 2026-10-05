import { CATEGORIES, TOOLS } from './toolsData.js';
import { renderToolUI } from './toolHandlers.js';
import { extractVideoId, thumbnailUrl, getAllThumbnails } from './youtube.js';
import { extractInstagramCode, getInstagramThumbnails } from './instagram.js';
import { parseVideoInfo } from './videoDownloader.js';

// DOM Selectors
const $ = (selector) => document.querySelector(selector);
const $$ = (selector) => document.querySelectorAll(selector);

// State
let activeCategory = 'all';
let searchQuery = '';
let favorites = new Set(JSON.parse(localStorage.getItem('omnitools-favorites') || '["yt-thumb-grabber","ig-media-grabber","universal-video-downloader","word-counter","case-converter","qr-code-studio"]'));
let pageSize = 48;
let currentLimit = pageSize;
let activeHeroTab = 'yt';

// Toast Notification
export const showToast = (text) => {
  const toast = $('#toast');
  if (!toast) return;
  toast.textContent = text;
  toast.classList.add('show');
  clearTimeout(showToast.timer);
  showToast.timer = setTimeout(() => toast.classList.remove('show'), 2600);
};

// Theme initialization
const root = document.documentElement;
const savedTheme = localStorage.getItem('omnitools-theme');
const initialTheme = savedTheme || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'dark');
root.dataset.theme = initialTheme;

$('#theme-toggle')?.addEventListener('click', () => {
  const nextTheme = root.dataset.theme === 'dark' ? 'light' : 'dark';
  root.dataset.theme = nextTheme;
  localStorage.setItem('omnitools-theme', nextTheme);
  $('#theme-toggle').setAttribute('aria-label', `Switch to ${nextTheme === 'dark' ? 'light' : 'dark'} theme`);
});

// Category Filter Chips
function renderCategoryChips() {
  const chipsContainer = $('#category-chips');
  if (!chipsContainer) return;

  const totalAll = TOOLS.length;
  const favCount = favorites.size;

  let html = `
    <button class="category-chip ${activeCategory === 'all' ? 'active' : ''}" data-cat="all">
      <span>✨ All Tools</span>
      <span class="chip-count">${totalAll}</span>
    </button>
    <button class="category-chip ${activeCategory === 'favorites' ? 'active' : ''}" data-cat="favorites">
      <span>⭐ Favorites</span>
      <span class="chip-count">${favCount}</span>
    </button>
  `;

  CATEGORIES.forEach(cat => {
    const count = TOOLS.filter(t => t.category === cat.id).length;
    html += `
      <button class="category-chip ${activeCategory === cat.id ? 'active' : ''}" data-cat="${cat.id}">
        <span>${cat.name}</span>
        <span class="chip-count">${count}</span>
      </button>
    `;
  });

  chipsContainer.innerHTML = html;

  chipsContainer.querySelectorAll('.category-chip').forEach(btn => {
    btn.onclick = () => {
      activeCategory = btn.dataset.cat;
      currentLimit = pageSize;
      renderCategoryChips();
      renderToolsList();
    };
  });
}

// Filter Tools
function getFilteredTools() {
  const q = searchQuery.trim().toLowerCase();
  return TOOLS.filter(t => {
    // Category check
    if (activeCategory === 'favorites') {
      if (!favorites.has(t.id)) return false;
    } else if (activeCategory !== 'all' && t.category !== activeCategory) {
      return false;
    }

    // Search query check
    if (!q) return true;
    return (
      t.name.toLowerCase().includes(q) ||
      t.desc.toLowerCase().includes(q) ||
      t.category.toLowerCase().includes(q) ||
      t.badge.toLowerCase().includes(q)
    );
  });
}

// Render Tools Grid
function renderToolsList() {
  const grid = $('#tools-grid');
  const countEl = $('#tools-count-display');
  const loadMoreBtn = $('#load-more-btn');
  if (!grid) return;

  const filtered = getFilteredTools();
  const visible = filtered.slice(0, currentLimit);

  if (countEl) {
    countEl.innerHTML = `Showing <strong>${visible.length.toLocaleString()}</strong> of <strong>${filtered.length.toLocaleString()}</strong> tools (Total: ${TOOLS.length.toLocaleString()}+)`;
  }

  if (visible.length === 0) {
    grid.innerHTML = `
      <div style="grid-column: 1 / -1; text-align: center; padding: 3rem 1rem;">
        <h3>No tools found matching "${searchQuery}"</h3>
        <p class="small-hint">Try searching for keywords like "thumbnail", "download", "format", "password", "converter", or "calculator".</p>
      </div>
    `;
    if (loadMoreBtn) loadMoreBtn.style.display = 'none';
    return;
  }

  grid.innerHTML = visible.map(tool => {
    const isFav = favorites.has(tool.id);
    return `
      <div class="tool-card" data-id="${tool.id}">
        <div>
          <div class="tool-card-top">
            <div class="tool-card-badges">
              <span class="tool-badge badge-${tool.badge.toLowerCase()}">${tool.badge}</span>
            </div>
            <button class="fav-btn ${isFav ? 'active' : ''}" data-favid="${tool.id}" title="${isFav ? 'Remove from favorites' : 'Add to favorites'}">
              <svg viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
            </button>
          </div>
          <h3 class="tool-title">${tool.name}</h3>
          <p class="tool-desc">${tool.desc}</p>
        </div>
        <div class="tool-card-footer">
          <span class="tool-card-category">${tool.category}</span>
          <button class="tool-open-btn">Open Tool →</button>
        </div>
      </div>
    `;
  }).join('');

  // Favorites clicks
  grid.querySelectorAll('.fav-btn').forEach(btn => {
    btn.onclick = (e) => {
      e.stopPropagation();
      const id = btn.dataset.favid;
      if (favorites.has(id)) {
        favorites.delete(id);
        btn.classList.remove('active');
        showToast('Removed from favorites');
      } else {
        favorites.add(id);
        btn.classList.add('active');
        showToast('Added to favorites!');
      }
      localStorage.setItem('omnitools-favorites', JSON.stringify([...favorites]));
      renderCategoryChips();
    };
  });

  // Tool card clicks
  grid.querySelectorAll('.tool-card').forEach(card => {
    card.onclick = () => {
      const id = card.dataset.id;
      const tool = TOOLS.find(t => t.id === id);
      if (tool) openToolModal(tool);
    };
  });

  // Load more button visibility
  if (loadMoreBtn) {
    if (visible.length < filtered.length) {
      loadMoreBtn.style.display = 'inline-block';
      loadMoreBtn.textContent = `Load More Tools (${filtered.length - visible.length} remaining)`;
    } else {
      loadMoreBtn.style.display = 'none';
    }
  }
}

// Modal open/close
function openToolModal(tool) {
  const modal = $('#tool-modal');
  const container = $('#modal-tool-container');
  if (!modal || !container) return;

  renderToolUI(tool, container, showToast);
  modal.classList.add('active');
  document.body.style.overflow = 'hidden';
}

function closeToolModal() {
  const modal = $('#tool-modal');
  if (!modal) return;
  modal.classList.remove('active');
  document.body.style.overflow = '';
}

// Flagship Fast Launcher in Hero Box
function renderFlagshipHero(tab) {
  activeHeroTab = tab;
  const frame = $('#flagship-tool-frame');
  if (!frame) return;

  $$('.flagship-tabs .tab-btn').forEach(b => {
    b.classList.toggle('active', b.dataset.tab === tab);
  });

  if (tab === 'yt') {
    const ytTool = TOOLS.find(t => t.id === 'yt-thumb-grabber') || TOOLS[0];
    renderToolUI(ytTool, frame, showToast);
  } else if (tab === 'ig') {
    const igTool = TOOLS.find(t => t.id === 'ig-media-grabber') || TOOLS[1];
    renderToolUI(igTool, frame, showToast);
  } else if (tab === 'video') {
    const vidTool = TOOLS.find(t => t.id === 'universal-video-downloader') || TOOLS[2];
    renderToolUI(vidTool, frame, showToast);
  }
}

// Initialize Application
document.addEventListener('DOMContentLoaded', () => {
  renderCategoryChips();
  renderToolsList();
  renderFlagshipHero('yt');

  // Search input
  const searchInput = $('#search-input');
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      searchQuery = e.target.value;
      currentLimit = pageSize;
      renderToolsList();
    });
  }

  // Global keyboard shortcuts
  window.addEventListener('keydown', (e) => {
    if ((e.key === '/' || (e.ctrlKey && e.key === 'k') || (e.metaKey && e.key === 'k')) && document.activeElement !== searchInput) {
      e.preventDefault();
      searchInput?.focus();
      searchInput?.select();
    }
    if (e.key === 'Escape') {
      closeToolModal();
    }
  });

  // Load more button
  $('#load-more-btn')?.addEventListener('click', () => {
    currentLimit += pageSize;
    renderToolsList();
  });

  // Modal close handlers
  $('#modal-close-btn')?.addEventListener('click', closeToolModal);
  $('#tool-modal')?.addEventListener('click', (e) => {
    if (e.target.id === 'tool-modal') closeToolModal();
  });

  // Hero tabs
  $$('.flagship-tabs .tab-btn').forEach(btn => {
    btn.onclick = () => renderFlagshipHero(btn.dataset.tab);
  });

  // APK Download triggers
  $$('.apk-download-btn, #hero-apk-btn').forEach(btn => {
    btn.onclick = (e) => {
      e.preventDefault();
      const a = document.createElement('a');
      a.href = './omnitools-pro.apk';
      a.download = 'omnitools-pro.apk';
      a.click();
      showToast('Downloading OmniTools Pro Android APK...');
    };
  });
});
