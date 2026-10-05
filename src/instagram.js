/**
 * Instagram Thumbnail & Media Grabber
 */

const IG_SHORTCODE_REGEX = /(?:https?:\/\/)?(?:www\.)?instagram\.com\/(?:p|reel|reels|tv)\/([a-zA-Z0-9_-]+)/;
const IG_USERNAME_REGEX = /(?:https?:\/\/)?(?:www\.)?instagram\.com\/([a-zA-Z0-9_.]+)/;

export function extractInstagramCode(input) {
  if (!input) return null;
  const value = input.trim();
  const match = value.match(IG_SHORTCODE_REGEX);
  if (match && match[1]) {
    return {
      type: value.includes('/reel') ? 'reel' : value.includes('/tv') ? 'tv' : 'post',
      shortcode: match[1]
    };
  }
  // Check if it's a bare shortcode
  if (/^[a-zA-Z0-9_-]{10,12}$/.test(value)) {
    return { type: 'post', shortcode: value };
  }
  // Check if it's a username profile
  const userMatch = value.match(IG_USERNAME_REGEX);
  if (userMatch && userMatch[1] && !['p', 'reel', 'reels', 'tv', 'stories', 'explore', 'direct'].includes(userMatch[1])) {
    return { type: 'profile', username: userMatch[1] };
  }
  return null;
}

export function getInstagramThumbnails(shortcode) {
  if (!shortcode) return [];
  // Instagram public media redirection endpoints
  return [
    {
      quality: 'large',
      name: 'High Definition (Large)',
      resolution: '1080 × 1080 (HD)',
      badge: 'Full HD',
      url: `https://www.instagram.com/p/${shortcode}/media/?size=l`,
      note: 'Full original resolution post/reel cover'
    },
    {
      quality: 'medium',
      name: 'Medium Quality',
      resolution: '640 × 640',
      badge: 'Standard',
      url: `https://www.instagram.com/p/${shortcode}/media/?size=m`,
      note: 'Optimized for mobile viewing'
    },
    {
      quality: 'thumb',
      name: 'Thumbnail Grid',
      resolution: '320 × 320',
      badge: 'Thumbnail',
      url: `https://www.instagram.com/p/${shortcode}/media/?size=t`,
      note: 'Grid thumbnail version'
    }
  ];
}

const POPULAR_HASHTAGS = {
  general: ['#explorepage', '#viral', '#trending', '#instagood', '#photooftheday', '#reels', '#reelsinstagram', '#fyp', '#instadaily', '#picoftheday'],
  tech: ['#tech', '#coding', '#developer', '#programming', '#webdev', '#software', '#technology', '#javascript', '#python', '#cybersecurity'],
  fitness: ['#fitness', '#workout', '#gym', '#fitfam', '#bodybuilding', '#health', '#motivation', '#personaltrainer', '#lifestyle', '#fitlife'],
  photography: ['#photography', '#photo', '#photographer', '#nature', '#streetphotography', '#portrait', '#visualsoflife', '#camera', '#art', '#lightroom'],
  travel: ['#travel', '#travelphotography', '#wanderlust', '#travelgram', '#vacation', '#adventure', '#nature', '#explore', '#instatravel', '#trip'],
  business: ['#business', '#entrepreneur', '#marketing', '#success', '#money', '#digitalmarketing', '#branding', '#motivation', '#startup', '#smallbusiness']
};

export function getTrendingHashtags(niche = 'general') {
  return POPULAR_HASHTAGS[niche] || POPULAR_HASHTAGS.general;
}
