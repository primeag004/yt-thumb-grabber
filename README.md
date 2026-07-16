# ThumbCatch

A fast, polished, and privacy-friendly YouTube thumbnail grabber. Paste a YouTube URL, choose a quality, and download the image—no backend or account required.

## Features

- Supports watch, short, share, embed, and live YouTube links
- Max-resolution, standard, and high-quality thumbnail options
- Automatic fallback when max resolution is unavailable
- Direct download with graceful browser fallback
- Copy-to-clipboard action
- Responsive, accessible interface with dark mode
- Zero runtime dependencies and no tracking

## Development

```bash
npm install
npm run dev
```

## Quality checks

```bash
npm test
npm run build
```

## How it works

YouTube exposes public thumbnail images through `i.ytimg.com`. ThumbCatch extracts the 11-character video ID locally in your browser and builds the corresponding image URL. No pasted links or personal data are sent to this application.

> Thumbnails may be copyrighted. Only download and use images you own or have permission to use.
