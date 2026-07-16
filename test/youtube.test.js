import test from 'node:test';
import assert from 'node:assert/strict';
import { extractVideoId, thumbnailUrl } from '../src/youtube.js';

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
