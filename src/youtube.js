const ID_PATTERN = /^[a-zA-Z0-9_-]{11}$/;

export function extractVideoId(input) {
  if (!input) return null;
  const value = input.trim();
  if (ID_PATTERN.test(value)) return value;

  let url;
  try {
    url = new URL(value.startsWith('http') ? value : `https://${value}`);
  } catch {
    return null;
  }

  const host = url.hostname.replace(/^www\./, '').replace(/^m\./, '');
  let candidate = null;
  if (host === 'youtu.be') candidate = url.pathname.split('/').filter(Boolean)[0];
  if (host === 'youtube.com' || host.endsWith('.youtube.com')) {
    candidate = url.searchParams.get('v');
    if (!candidate) {
      const parts = url.pathname.split('/').filter(Boolean);
      if (['shorts', 'embed', 'live'].includes(parts[0])) candidate = parts[1];
    }
  }
  return candidate && ID_PATTERN.test(candidate) ? candidate : null;
}

export function thumbnailUrl(videoId, quality = 'maxresdefault') {
  return `https://i.ytimg.com/vi/${videoId}/${quality}.jpg`;
}

export function getAllThumbnails(videoId) {
  if (!videoId) return [];
  return [
    {
      quality: 'maxresdefault',
      name: 'Ultra HD (4K / 1080p)',
      resolution: '1280 × 720',
      badge: 'Maximum',
      url: `https://i.ytimg.com/vi/${videoId}/maxresdefault.jpg`,
      webp: `https://i.ytimg.com/vi_webp/${videoId}/maxresdefault.webp`
    },
    {
      quality: 'sddefault',
      name: 'Standard Definition (SD)',
      resolution: '640 × 480',
      badge: 'High Quality',
      url: `https://i.ytimg.com/vi/${videoId}/sddefault.jpg`,
      webp: `https://i.ytimg.com/vi_webp/${videoId}/sddefault.webp`
    },
    {
      quality: 'hqdefault',
      name: 'High Quality (HQ)',
      resolution: '480 × 360',
      badge: 'HQ',
      url: `https://i.ytimg.com/vi/${videoId}/hqdefault.jpg`,
      webp: `https://i.ytimg.com/vi_webp/${videoId}/hqdefault.webp`
    },
    {
      quality: 'mqdefault',
      name: 'Medium Quality (MQ)',
      resolution: '320 × 180',
      badge: 'Medium',
      url: `https://i.ytimg.com/vi/${videoId}/mqdefault.jpg`,
      webp: `https://i.ytimg.com/vi_webp/${videoId}/mqdefault.webp`
    },
    {
      quality: 'default',
      name: 'Normal Thumbnail',
      resolution: '120 × 90',
      badge: 'Small',
      url: `https://i.ytimg.com/vi/${videoId}/default.jpg`,
      webp: `https://i.ytimg.com/vi_webp/${videoId}/default.webp`
    }
  ];
}

export function getYouTubeEmbedUrl(videoId) {
  return `https://www.youtube-nocookie.com/embed/${videoId}`;
}
