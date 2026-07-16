const ID_PATTERN = /^[a-zA-Z0-9_-]{11}$/;

export function extractVideoId(input) {
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
