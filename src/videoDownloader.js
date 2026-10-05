/**
 * Universal Video & Media Link Extractor
 */

export function detectPlatform(input) {
  if (!input) return null;
  const url = input.trim();

  if (/youtube\.com|youtu\.be/i.test(url)) return 'youtube';
  if (/instagram\.com/i.test(url)) return 'instagram';
  if (/tiktok\.com/i.test(url)) return 'tiktok';
  if (/twitter\.com|x\.com/i.test(url)) return 'twitter';
  if (/pinterest\.com|pin\.it/i.test(url)) return 'pinterest';
  if (/reddit\.com/i.test(url)) return 'reddit';
  if (/vimeo\.com/i.test(url)) return 'vimeo';
  if (/facebook\.com|fb\.watch/i.test(url)) return 'facebook';
  if (/dailymotion\.com|dai\.ly/i.test(url)) return 'dailymotion';
  if (/twitch\.tv/i.test(url)) return 'twitch';
  if (/threads\.net/i.test(url)) return 'threads';
  if (/soundcloud\.com/i.test(url)) return 'soundcloud';

  return 'generic';
}

export function parseVideoInfo(input) {
  if (!input) return null;
  const url = input.trim();
  const platform = detectPlatform(url);

  switch (platform) {
    case 'tiktok': {
      const match = url.match(/video\/(\d+)/) || url.match(/\/v\/(\d+)/);
      const id = match ? match[1] : 'tiktok-video';
      return {
        platform: 'TikTok',
        id,
        badge: 'TikTok Video',
        preview: 'https://images.unsplash.com/photo-1611162617213-7d7a39e9b1d7?w=600&auto=format&fit=crop&q=80',
        qualities: [
          { name: 'HD No Watermark (Direct Stream)', format: 'MP4 · 1080p', type: 'video' },
          { name: 'Original Watermarked', format: 'MP4 · 720p', type: 'video' },
          { name: 'Audio Track / Sound Only', format: 'MP3 · 320kbps', type: 'audio' }
        ],
        rawUrl: url
      };
    }
    case 'twitter': {
      const match = url.match(/status\/(\d+)/);
      const id = match ? match[1] : 'tweet-id';
      return {
        platform: 'Twitter / X',
        id,
        badge: 'X Post',
        preview: 'https://images.unsplash.com/photo-1611605698335-8b1569810432?w=600&auto=format&fit=crop&q=80',
        qualities: [
          { name: 'High Quality 1080p', format: 'MP4 · 1920 × 1080', type: 'video' },
          { name: 'Medium Quality 720p', format: 'MP4 · 1280 × 720', type: 'video' },
          { name: 'Mobile Quality 480p', format: 'MP4 · 640 × 480', type: 'video' }
        ],
        rawUrl: url
      };
    }
    case 'pinterest': {
      return {
        platform: 'Pinterest',
        id: 'pin-media',
        badge: 'Pin Media',
        preview: 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=600&auto=format&fit=crop&q=80',
        qualities: [
          { name: 'Original High-Res Video', format: 'MP4 · Full HD', type: 'video' },
          { name: 'Original High-Res Image Pin', format: 'JPG / PNG · Ultra HD', type: 'image' }
        ],
        rawUrl: url
      };
    }
    case 'vimeo': {
      const match = url.match(/vimeo\.com\/(\d+)/);
      const id = match ? match[1] : '';
      return {
        platform: 'Vimeo',
        id,
        badge: 'Vimeo HD',
        preview: id ? `https://vumbnail.com/${id}.jpg` : 'https://images.unsplash.com/photo-1574717024653-61fd2cf4d44d?w=600&auto=format&fit=crop&q=80',
        qualities: [
          { name: '1080p Full HD', format: 'MP4 · 1080p', type: 'video' },
          { name: '720p HD', format: 'MP4 · 720p', type: 'video' },
          { name: 'High Res Thumbnail Cover', format: 'JPG · 1280 × 720', type: 'image' }
        ],
        rawUrl: url
      };
    }
    case 'reddit': {
      return {
        platform: 'Reddit',
        id: 'reddit-post',
        badge: 'Reddit Media',
        preview: 'https://images.unsplash.com/photo-1581291518857-4e27b48ff24e?w=600&auto=format&fit=crop&q=80',
        qualities: [
          { name: 'Video with Merged Audio', format: 'MP4 · 1080p', type: 'video' },
          { name: 'Original GIF / Image', format: 'GIF / PNG', type: 'image' },
          { name: 'Audio Track Only', format: 'AAC / MP3', type: 'audio' }
        ],
        rawUrl: url
      };
    }
    case 'facebook': {
      return {
        platform: 'Facebook',
        id: 'fb-video',
        badge: 'FB Reel / Video',
        preview: 'https://images.unsplash.com/photo-1563986768609-322da13575f3?w=600&auto=format&fit=crop&q=80',
        qualities: [
          { name: 'HD Video Stream', format: 'MP4 · 1080p', type: 'video' },
          { name: 'SD Video Stream', format: 'MP4 · 480p', type: 'video' }
        ],
        rawUrl: url
      };
    }
    case 'dailymotion': {
      const match = url.match(/video\/([a-zA-Z0-9]+)/);
      const id = match ? match[1] : '';
      return {
        platform: 'Dailymotion',
        id,
        badge: 'Dailymotion',
        preview: id ? `https://www.dailymotion.com/thumbnail/video/${id}` : 'https://images.unsplash.com/photo-1574717024653-61fd2cf4d44d?w=600&auto=format&fit=crop&q=80',
        qualities: [
          { name: '1080p Stream', format: 'MP4 · 1080p', type: 'video' },
          { name: '720p Stream', format: 'MP4 · 720p', type: 'video' },
          { name: 'Video Thumbnail', format: 'JPG · HD', type: 'image' }
        ],
        rawUrl: url
      };
    }
    default: {
      return {
        platform: 'Universal Stream',
        id: 'generic-media',
        badge: 'Universal',
        preview: 'https://images.unsplash.com/photo-1492691527719-9d1e07e534b4?w=600&auto=format&fit=crop&q=80',
        qualities: [
          { name: 'Direct Video Stream', format: 'MP4 / WEBM', type: 'video' },
          { name: 'Audio Track', format: 'MP3 / M4A', type: 'audio' },
          { name: 'Cover / Thumbnail Poster', format: 'JPG / PNG', type: 'image' }
        ],
        rawUrl: url
      };
    }
  }
}
