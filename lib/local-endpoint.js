const LOCAL_HOSTS = new Set(['localhost', '127.0.0.1', '::1', '[::1]']);

/**
 * Parses an API base URL and guarantees that the proxy cannot be used to send
 * chat content anywhere other than the current device.
 */
export function localEndpoint(value) {
  let url;
  try {
    url = new URL(String(value || '').trim());
  } catch {
    return null;
  }
  if (!['http:', 'https:'].includes(url.protocol) || !LOCAL_HOSTS.has(url.hostname.toLowerCase())) return null;
  url.username = '';
  url.password = '';
  url.hash = '';
  return url;
}

export function apiUrl(base, path) {
  const url = new URL(base);
  const prefix = url.pathname.endsWith('/') ? url.pathname : `${url.pathname}/`;
  url.pathname = `${prefix}${path.replace(/^\//, '')}`.replace(/\/+/g, '/');
  url.search = '';
  return url;
}

export function defaultEndpoint(provider) {
  return provider === 'openai' ? 'http://127.0.0.1:8080/v1' : 'http://127.0.0.1:11434';
}
