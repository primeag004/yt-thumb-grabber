import test from 'node:test';
import assert from 'node:assert/strict';
import { extractVideoId, thumbnailUrl, getAllThumbnails } from '../src/youtube.js';
import { extractInstagramCode, getInstagramThumbnails } from '../src/instagram.js';
import { detectPlatform, parseVideoInfo } from '../src/videoDownloader.js';
import { TOOLS, CATEGORIES } from '../src/toolsData.js';

// YouTube tests
const id = 'dQw4w9WgXcQ';
const cases = [
  `https://www.youtube.com/watch?v=${id}`,
  `https://youtu.be/${id}?si=abc`,
  `https://youtube.com/shorts/${id}`,
  `https://www.youtube.com/embed/${id}`,
  `https://youtube.com/live/${id}`,
  `youtube.com/watch?v=${id}`,
  id,
];
for (const value of cases) test(`extracts ID from ${value}`, () => assert.equal(extractVideoId(value), id));

test('rejects invalid input', () => {
  assert.equal(extractVideoId('not a youtube link'), null);
  assert.equal(extractVideoId('https://example.com/watch?v=dQw4w9WgXcQ'), null);
});

test('builds thumbnail URL', () => assert.equal(thumbnailUrl(id, 'hqdefault'), `https://i.ytimg.com/vi/${id}/hqdefault.jpg`));

test('gets all YouTube thumbnail resolutions', () => {
  const thumbs = getAllThumbnails(id);
  assert.equal(thumbs.length, 5);
  assert.equal(thumbs[0].quality, 'maxresdefault');
  assert.ok(thumbs[0].url.includes('maxresdefault.jpg'));
});

// Instagram tests
test('extracts Instagram shortcode from reel link', () => {
  const res = extractInstagramCode('https://www.instagram.com/reel/C7xyz123abc/?utm_source=ig_web');
  assert.ok(res);
  assert.equal(res.shortcode, 'C7xyz123abc');
  assert.equal(res.type, 'reel');
});

test('extracts Instagram shortcode from post link', () => {
  const res = extractInstagramCode('https://www.instagram.com/p/DFzL123abc/');
  assert.ok(res);
  assert.equal(res.shortcode, 'DFzL123abc');
  assert.equal(res.type, 'post');
});

test('gets Instagram thumbnail qualities', () => {
  const thumbs = getInstagramThumbnails('DFzL123abc');
  assert.equal(thumbs.length, 3);
  assert.ok(thumbs[0].url.includes('DFzL123abc'));
});

// Video Downloader platform detection tests
test('detects TikTok video links', () => {
  assert.equal(detectPlatform('https://www.tiktok.com/@user/video/72123456789'), 'tiktok');
});

test('detects Twitter / X links', () => {
  assert.equal(detectPlatform('https://x.com/user/status/1789123456'), 'twitter');
});

test('detects Vimeo links', () => {
  assert.equal(detectPlatform('https://vimeo.com/76979871'), 'vimeo');
});

test('parses video stream info', () => {
  const info = parseVideoInfo('https://vimeo.com/76979871');
  assert.ok(info);
  assert.equal(info.platform, 'Vimeo');
  assert.ok(info.qualities.length >= 2);
});

// 1500+ Tools verification
test('verifies total tool count is >= 1500', () => {
  assert.ok(TOOLS.length >= 1500, `Expected at least 1500 tools, found ${TOOLS.length}`);
  assert.ok(CATEGORIES.length === 12, 'Expected 12 categories');
});
