import json

CATEGORIES = [
    {
        "id": "media",
        "name": "📸 Media & Thumbnails",
        "shortName": "Media",
        "desc": "YouTube, Instagram, TikTok, and universal video downloader & thumbnail grabber suite.",
        "icon": "video"
    },
    {
        "id": "image",
        "name": "🖼️ Image & Graphics",
        "shortName": "Image",
        "desc": "Convert, resize, compress, crop, and apply stunning visual filters and effects.",
        "icon": "image"
    },
    {
        "id": "text",
        "name": "📝 Text & Content",
        "shortName": "Text",
        "desc": "Word counters, text case converters, string utilities, diff checkers, and voice tools.",
        "icon": "type"
    },
    {
        "id": "developer",
        "name": "💻 Developer & Web",
        "shortName": "Developer",
        "desc": "JSON tools, regex testers, minifiers, cURL converters, CSS generators, and web utilities.",
        "icon": "code"
    },
    {
        "id": "security",
        "name": "🔒 Security & Cryptography",
        "shortName": "Security",
        "desc": "Strong password generators, cryptographic hashes, ciphers, and privacy checkers.",
        "icon": "shield"
    },
    {
        "id": "social",
        "name": "📱 Social Media & SEO",
        "shortName": "Social & SEO",
        "desc": "Trending hashtags, character limits, UTM builders, OpenGraph cards, and bio links.",
        "icon": "share"
    },
    {
        "id": "qr",
        "name": "🔲 QR Codes & Barcodes",
        "shortName": "QR & Barcode",
        "desc": "Custom QR code generator with colors, barcode makers, WiFi codes, and scanner tools.",
        "icon": "grid"
    },
    {
        "id": "calculator",
        "name": "🧮 Calculators & Math",
        "shortName": "Calculators",
        "desc": "Scientific calculator, EMI loan formulas, discounts, taxes, percentages, and math tools.",
        "icon": "calculator"
    },
    {
        "id": "converter",
        "name": "⚖️ Unit & Currency",
        "shortName": "Converters",
        "desc": "Universal converter for length, mass, temperature, data storage, speed, and volume.",
        "icon": "repeat"
    },
    {
        "id": "time",
        "name": "⏱️ Time & Productivity",
        "shortName": "Time & Date",
        "desc": "Unix timestamps, world clock, age calculator, date difference, stopwatches, and timers.",
        "icon": "clock"
    },
    {
        "id": "audio",
        "name": "🎵 Audio & Voice Studio",
        "shortName": "Audio Studio",
        "desc": "Frequency tone generators, audio metronome, tap BPM counter, and voice recorder.",
        "icon": "music"
    },
    {
        "id": "health",
        "name": "🩺 Health & Fitness",
        "shortName": "Health",
        "desc": "BMI calculator, BMR, TDEE, body fat estimator, sleep cycles, and calorie estimators.",
        "icon": "activity"
    }
]

# We will generate comprehensive lists of tools for each category totaling 1500+ tools!
# Each tool has id, name, category, desc, badge, type, inputs/config.

tools = []

# 1. Media & Thumbnails
media_tools = [
    ("yt-thumb-grabber", "YouTube Thumbnail Grabber Pro", "Download YouTube thumbnails in 4K, 1080p, 720p, HQ, and WebP formats instantly.", "FLAGSHIP", "special-yt"),
    ("ig-media-grabber", "Instagram Thumbnail & Media Grabber", "Extract Reels covers, post thumbnails, IGTV, and profile pictures in Full HD.", "FLAGSHIP", "special-ig"),
    ("universal-video-downloader", "Universal Video & Audio Downloader", "Download preview, stream, and audio from TikTok, X, Pinterest, Vimeo, Reddit, and FB.", "FLAGSHIP", "special-video"),
    ("yt-shorts-grabber", "YouTube Shorts Cover Grabber", "Extract high-resolution vertical 9:16 cover images from any YouTube Short.", "HOT", "special-yt"),
    ("yt-channel-art", "YouTube Channel Banner Grabber", "Retrieve YouTube channel banner artwork in maximum 2560x1440 resolution.", "POPULAR", "special-yt"),
    ("yt-channel-avatar", "YouTube Channel Logo & Avatar Grabber", "Download original 800x800 high-res channel profile pictures.", "NEW", "special-yt"),
    ("yt-embed-generator", "YouTube Privacy Embed Code Generator", "Generate responsive, privacy-enhanced youtube-nocookie embed iframe codes.", "PRO", "special-yt"),
    ("yt-timestamp-maker", "YouTube Timestamp Link Generator", "Create shareable YouTube links that jump directly to a precise timestamp.", "FAST", "special-yt"),
    ("yt-tags-extractor", "YouTube Tags & Keywords Extractor", "Extract metadata tags and SEO search keywords from any YouTube video URL.", "SEO", "special-yt"),
    ("ig-reels-cover", "Instagram Reels Cover Art Grabber", "Extract high quality reel thumbnail covers without UI overlays.", "HOT", "special-ig"),
    ("ig-profile-pic", "Instagram Profile Picture HD Viewer", "View and download full-size Instagram profile avatars in original clarity.", "POPULAR", "special-ig"),
    ("ig-carousel-slides", "Instagram Carousel Slides Inspector", "Inspect multi-slide carousel posts and extract individual slide images.", "PRO", "special-ig"),
    ("tiktok-video-grabber", "TikTok Video Without Watermark", "Get clean TikTok video preview and download links without watermark.", "HOT", "special-video"),
    ("tiktok-audio-extractor", "TikTok Sound / MP3 Extractor", "Extract background audio tracks and trending sounds from TikTok videos.", "AUDIO", "special-video"),
    ("tiktok-profile-pic", "TikTok Profile Picture HD Grabber", "Download uncompressed TikTok creator avatar pictures in high definition.", "NEW", "special-video"),
    ("twitter-video-downloader", "Twitter / X Video & GIF Grabber", "Extract MP4 video and animated GIF download links from any Tweet URL.", "POPULAR", "special-video"),
    ("pinterest-media-grabber", "Pinterest Video & Pin HD Grabber", "Download 1080p video pins and ultra high resolution image boards.", "PRO", "special-video"),
    ("reddit-video-audio", "Reddit Video with Audio Merger", "Extract Reddit video streams with synchronized audio tracks.", "HOT", "special-video"),
    ("vimeo-thumb-grabber", "Vimeo HD Thumbnail & Cover Grabber", "Grab official high-resolution 1080p thumbnail posters from Vimeo videos.", "FAST", "special-video"),
    ("dailymotion-thumb", "Dailymotion Video Thumbnail Grabber", "Extract HQ video preview stills and thumbnails from Dailymotion URLs.", "NEW", "special-video"),
    ("facebook-reel-grabber", "Facebook Reel & Video Cover Grabber", "Extract video posters and thumbnail previews from Facebook Reels and videos.", "PRO", "special-video"),
    ("threads-media-grabber", "Threads Post Media & Cover Grabber", "Download images and video clips shared on Meta Threads posts.", "NEW", "special-video"),
    ("twitch-clip-downloader", "Twitch Clip & VOD Thumbnail Grabber", "Grab high-definition thumbnails and download links for Twitch stream clips.", "GAMING", "special-video"),
    ("soundcloud-artwork", "SoundCloud Track Artwork Grabber", "Download original 500x500 high-res album cover art from SoundCloud tracks.", "MUSIC", "special-video"),
    ("spotify-cover-grabber", "Spotify Album Art & Canvas Grabber", "Extract original Spotify album art and playlist covers in full resolution.", "MUSIC", "special-video")
]

for item in media_tools:
    tools.append({
        "id": item[0],
        "name": item[1],
        "category": "media",
        "desc": item[2],
        "badge": item[3],
        "type": item[4],
        "icon": "video"
    })

# Add procedural specialized tools to reach target counts per category
target_per_category = {
    "media": 130,
    "image": 130,
    "text": 130,
    "developer": 135,
    "security": 125,
    "social": 125,
    "qr": 120,
    "calculator": 130,
    "converter": 125,
    "time": 120,
    "audio": 125,
    "health": 135
}

# Sub-tool templates for media
media_sub_types = [
    ("Video Resolution Scaler", "Calculate scaled video resolutions (4K, 1440p, 1080p, 720p, 480p, 360p, 240p) maintaining aspect ratio.", "calculator"),
    ("Video Bitrate Calculator", "Estimate optimal video bitrates for streaming and recording across different frame rates.", "calculator"),
    ("Audio Bitrate Estimator", "Calculate uncompressed and compressed audio file sizes based on sample rate and bit depth.", "calculator"),
    ("Aspect Ratio Calculator", "Determine 16:9, 4:3, 21:9, 9:16, 1:1 width and height dimensions with pixel precision.", "calculator"),
    ("Frame Rate & Timecode Calculator", "Convert between SMPTE timecodes, frames, seconds, and milliseconds at 24, 30, 60 fps.", "calculator"),
    ("SubRip (SRT) Subtitle Time Offset", "Shift subtitle timings forward or backward by custom milliseconds.", "text-transform"),
    ("Video File Size Estimator", "Estimate final output video file sizes from duration, video bitrate, and audio bitrate.", "calculator"),
    ("Social Video Dimensions Guide", "Quick dimensional reference for Reels, TikTok, Shorts, Stories, Feed, and Banner videos.", "reference"),
    ("YouTube Safe Zone Guide", "Overlay coordinates for YouTube mobile and desktop safe zones for channel art.", "reference"),
    ("Instagram Aspect Ratio Guide", "Aspect ratios and dimension guidelines for portraits (4:5), squares (1:1), and stories (9:16).", "reference"),
    ("GIF Frame Delay Calculator", "Calculate frame delay in hundredths of a second from target frames per second.", "calculator"),
    ("Video Stream Inspector", "Inspect video MIME types, codecs (H.264, HEVC, AV1, VP9), and container formats.", "analyzer"),
    ("Color Space Video Reference", "Reference guide for Rec.709, DCI-P3, and Rec.2020 color gamuts and HDR profiles.", "reference"),
    ("Audio Sample Rate Converter Reference", "Reference table comparing 44.1kHz, 48kHz, 96kHz, and 192kHz audio sample rates.", "reference"),
    ("Audio Loudness (LUFS) Estimator", "Estimate integrated loudness targets for YouTube (-14 LUFS), Spotify (-14 LUFS), and Apple Music.", "calculator")
]

idx = len(media_tools) + 1
for title, desc, ttype in media_sub_types:
    tools.append({
        "id": f"media-tool-{idx}",
        "name": title,
        "category": "media",
        "desc": desc,
        "badge": "PRO" if idx % 3 == 0 else "NEW" if idx % 2 == 0 else "FAST",
        "type": ttype,
        "icon": "video"
    })
    idx += 1

platforms = ["YouTube", "Instagram", "TikTok", "Twitter/X", "Pinterest", "Reddit", "Facebook", "Vimeo", "Twitch", "Dailymotion", "SoundCloud", "Spotify", "Snapchat", "Threads", "Tumblr", "LinkedIn", "Telegram", "Discord", "Flickr", "Behance", "Dribbble", "ArtStation", "Mixcloud", "Bandcamp", "Mastodon"]
media_actions = [
    ("Thumbnail Resizer", "Resize downloaded thumbnail covers to platform optimal dimensions.", "image-tool"),
    ("Cover Color Palette", "Extract dominant color swatches and hex codes from video cover art.", "image-tool"),
    ("Aspect Ratio Formatter", "Calculate exact cropping borders to fit 16:9 thumbnails into 1:1 or 9:16 cards.", "calculator"),
    ("Video SEO Title Analyzer", "Analyze video title character length, power words, and click-through potential.", "text-transform"),
    ("Video Tag Cloud Generator", "Generate comma-separated keyword tag lists optimized for search discovery.", "generator"),
    ("Watermark Placement Guide", "Calculate exact pixel offsets for branding watermarks on video covers.", "calculator"),
    ("Audio Waveform Previewer", "Visualize simulated audio waveforms from volume levels.", "audio-tool")
]

for p in platforms:
    for act, desc, ttype in media_actions:
        if len([t for t in tools if t['category'] == 'media']) >= target_per_category['media']:
            break
        tools.append({
            "id": f"media-{p.lower().replace('/', '-')}-{act.lower().replace(' ', '-')}",
            "name": f"{p} {act}",
            "category": "media",
            "desc": f"{p} media utility: {desc}",
            "badge": "FAST",
            "type": ttype,
            "icon": "video"
        })

print("Media tools count:", len([t for t in tools if t['category'] == 'media']))

# 2. Image & Graphics (130)
image_base = [
    ("image-converter", "Universal Image Format Converter", "Convert images between JPG, PNG, WebP, SVG, AVIF, and BMP formats in browser.", "FLAGSHIP", "image-tool"),
    ("image-compressor", "Image Compressor & Quality Optimizer", "Compress images with live visual comparison, file size reduction, and slider.", "FLAGSHIP", "image-tool"),
    ("image-resizer", "Image Resizer & Aspect Ratio Locker", "Scale images by exact pixels or percentage with aspect ratio preservation.", "FLAGSHIP", "image-tool"),
    ("image-cropper", "Image Cropper & Circle Masker", "Crop images with presets for 16:9, 1:1, 4:5, 9:16, 2:1, or circular avatar crop.", "HOT", "image-tool"),
    ("color-palette-extractor", "Color Palette Extractor from Image", "Upload any image to extract dominant hex colors, RGB codes, and color swatches.", "FLAGSHIP", "image-tool"),
    ("image-to-base64", "Image to Base64 DataURI Converter", "Convert any image into a base64 Data URI string for HTML/CSS embedding.", "PRO", "image-tool"),
    ("base64-to-image", "Base64 DataURI to Image Converter", "Decode base64 Data URI strings back into previewable and downloadable images.", "PRO", "image-tool"),
    ("image-filters-studio", "Image Filters & Effects Studio", "Apply blur, brightness, contrast, grayscale, invert, sepia, and hue rotation.", "POPULAR", "image-tool"),
    ("favicon-generator", "Favicon & App Icon Generator", "Generate multi-size favicons (16x16, 32x32, 48x48, 180x180, 512x512) and ICO.", "PRO", "image-tool"),
    ("meme-generator", "Meme Generator Studio", "Add classic top and bottom impact text to images and download instant PNG memes.", "POPULAR", "image-tool"),
    ("css-box-shadow", "CSS Box Shadow & Glow Generator", "Create realistic drop shadows, inner shadows, and multi-layer neon glows.", "FLAGSHIP", "css-tool"),
    ("css-gradient-studio", "CSS Gradient Generator Studio", "Design linear, radial, and conic gradients with unlimited color stops and CSS copy.", "FLAGSHIP", "css-tool"),
    ("image-watermark", "Image Watermark & Copyright Stamper", "Add customizable text or logo watermarks with opacity and angle controls.", "PRO", "image-tool"),
    ("image-exif-viewer", "Image EXIF & Metadata Viewer", "View camera make, model, exposure, GPS, and date info from JPEG photos.", "SECURITY", "image-tool"),
    ("image-exif-stripper", "Image EXIF Stripper (Privacy Cleaner)", "Strip all private location and camera metadata from photos before sharing.", "PRIVACY", "image-tool"),
    ("svg-to-png", "SVG Code to PNG Converter", "Paste SVG XML code or upload an SVG to render and download crisp raster PNGs.", "DEV", "image-tool"),
    ("image-inverter", "Image Negative / Invert Colors", "Invert all pixel color values to create photographic negative effects.", "FAST", "image-tool"),
    ("black-white-converter", "Black & White High-Contrast Converter", "Convert photos into dramatic monochrome black and white photography.", "POPULAR", "image-tool"),
    ("pixel-art-generator", "Pixel Art & Mosaic Generator", "Turn any photo into retro 8-bit or 16-bit pixel art with customizable block size.", "FUN", "image-tool"),
    ("image-rotate-flip", "Image Rotate & Mirror Flip", "Rotate images 90°, 180°, 270° or mirror flip horizontally and vertically.", "FAST", "image-tool")
]

for item in image_base:
    tools.append({
        "id": item[0],
        "name": item[1],
        "category": "image",
        "desc": item[2],
        "badge": item[3],
        "type": item[4],
        "icon": "image"
    })

# Procedural image tools
img_formats = ["JPG", "PNG", "WebP", "AVIF", "BMP", "GIF", "SVG", "ICO", "TIFF", "HEIC"]
img_ops = [
    ("Optimizer", "Optimize compression tables for smaller file sizes without quality loss.", "image-tool"),
    ("Metadata Cleaner", "Remove embedded color profiles and camera metadata chunks.", "image-tool"),
    ("Dimension Scanner", "Read width, height, color depth, and aspect ratio from image headers.", "image-tool"),
    ("Thumbnail Maker", "Generate miniature preview thumbnails optimized for responsive grids.", "image-tool"),
    ("Color Inverter", "Invert RGB channels for inverted preview.", "image-tool"),
    ("Grayscale Converter", "Convert image color channels to luminance grayscale.", "image-tool"),
    ("Blur Effect", "Apply smooth Gaussian blur filter to image background.", "image-tool"),
    ("Contrast Booster", "Enhance dynamic contrast and clarity.", "image-tool"),
    ("Aspect Ratio Matcher", "Fit image to target aspect ratios with smart padding.", "image-tool"),
    ("Base64 Codec", "Encode and decode raw image buffers to base64 strings.", "image-tool"),
    ("Color Counter", "Count total distinct colors present in the pixel matrix.", "image-tool"),
    ("Border Adder", "Add custom color border frames with adjustable stroke widths.", "image-tool")
]

for fmt in img_formats:
    for op, desc, ttype in img_ops:
        if len([t for t in tools if t['category'] == 'image']) >= target_per_category['image']:
            break
        tools.append({
            "id": f"img-{fmt.lower()}-{op.lower().replace(' ', '-')}",
            "name": f"{fmt} {op}",
            "category": "image",
            "desc": f"{fmt} format utility: {desc}",
            "badge": "FAST",
            "type": ttype,
            "icon": "image"
        })

print("Image tools count:", len([t for t in tools if t['category'] == 'image']))

# 3. Text & Content (130)
text_base = [
    ("word-counter", "Word & Character Counter Pro", "Count words, characters, sentences, paragraphs, reading time, and speaking time.", "FLAGSHIP", "text-analyzer"),
    ("case-converter", "Text Case Converter (12 Formats)", "Convert text to UPPERCASE, lowercase, Title Case, camelCase, snake_case, etc.", "FLAGSHIP", "text-transform"),
    ("slug-generator", "URL Slug & Permalink Generator", "Generate clean, SEO-friendly URL slugs with delimiter and special char options.", "PRO", "text-transform"),
    ("text-diff-checker", "Text Diff & Comparison Checker", "Compare two text versions side-by-side with color-coded additions and deletions.", "FLAGSHIP", "diff-tool"),
    ("lorem-ipsum-generator", "Lorem Ipsum Dummy Text Generator", "Generate placeholder dummy paragraphs, sentences, words, and list items.", "POPULAR", "generator"),
    ("text-to-speech", "Text to Speech (TTS Voice Reader)", "Convert written text into natural spoken voice using customizable browser voices.", "FLAGSHIP", "speech-tool"),
    ("speech-to-text", "Speech to Text (Voice Dictation)", "Dictate text using your microphone with live speech recognition in real-time.", "PRO", "speech-tool"),
    ("markdown-previewer", "Markdown Live Editor & HTML Renderer", "Write GitHub-flavored Markdown with live HTML preview and instant HTML export.", "FLAGSHIP", "markdown-tool"),
    ("text-repeater", "Text Repeater & Pattern Multiplier", "Repeat words, phrases, or emojis up to 10,000 times with custom separators.", "FAST", "text-transform"),
    ("reverse-text", "Reverse Text & Upside Down Flipper", "Reverse character order, reverse word order, or flip letters upside-down.", "FUN", "text-transform"),
    ("duplicate-lines-remover", "Remove Duplicate Lines & Sorter", "Deduplicate text lines, trim empty spaces, and sort alphabetically or numerically.", "PRO", "text-transform"),
    ("whitespace-cleaner", "Whitespace & Empty Lines Cleaner", "Normalize double spaces, strip tabs, trim trailing spaces, and join lines.", "FAST", "text-transform"),
    ("find-replace-regex", "Find & Replace with RegEx Support", "Perform global text replacement using plain strings or regular expression patterns.", "PRO", "text-transform"),
    ("morse-code-codec", "Morse Code Translator & Sound Player", "Translate plain English to Morse code and Morse code back to readable text.", "POPULAR", "text-transform"),
    ("binary-text-codec", "Binary to Text & Text to Binary", "Convert ASCII text to 8-bit binary 0s and 1s and binary back to text.", "DEV", "text-transform"),
    ("hex-text-codec", "Hexadecimal to Text & Text to Hex", "Convert ASCII text to hex bytes and hex strings back to plain text.", "DEV", "text-transform"),
    ("rot13-cipher", "ROT13 & Caesar Cipher Tool", "Rotate alphabetical characters by 13 positions or custom Caesar shift offsets.", "SECURITY", "text-transform"),
    ("fancy-fonts-styler", "Fancy Unicode Fonts & Text Styler", "Generate aesthetic Unicode fonts (𝒞𝓊𝓇𝓈𝒾𝓋ℯ, 𝕲𝖔𝖙𝖍𝖎𝖈, 𝔹𝕠𝕝𝕕, 𝖲𝖺𝗇𝗌, 🅂🅀🅄🄰🅁🄴) for social bios.", "HOT", "text-transform"),
    ("word-frequency-analyzer", "Word Frequency & Keyword Density", "Analyze text to rank most frequently used words, density percentages, and metrics.", "SEO", "text-analyzer"),
    ("extract-emails-tool", "Email Address Extractor from Text", "Extract all valid email addresses from messy text, logs, or HTML code.", "PRO", "text-analyzer"),
    ("extract-urls-tool", "URL & Link Extractor from Text", "Extract every web URL, domain, and hyperlink from text documents.", "PRO", "text-analyzer"),
    ("random-word-picker", "Random Word & Name Picker", "Paste a list of names or words and pick random winners or shuffle ordering.", "FUN", "generator")
]

for item in text_base:
    tools.append({
        "id": item[0],
        "name": item[1],
        "category": "text",
        "desc": item[2],
        "badge": item[3],
        "type": item[4],
        "icon": "type"
    })

# Procedural text tools
text_sub_categories = [
    ("Acronym", "Generator", "Generate pronounceable acronyms from phrase initial letters.", "generator"),
    ("Anagram", "Solver", "Find all anagram permutations from an input word or phrase.", "text-transform"),
    ("Palindrome", "Checker", "Check whether words or sentences read the same backward and forward.", "text-analyzer"),
    ("Character", "Frequency", "Count occurrences and percentages of every alphabet character.", "text-analyzer"),
    ("Line", "Numberer", "Prefix every line in text with customizable line numbers and formatting.", "text-transform"),
    ("Prefix/Suffix", "Adder", "Append custom prefixes and suffixes to every line in a text block.", "text-transform"),
    ("Text", "Shuffler", "Randomly shuffle line order or word order in paragraphs.", "text-transform"),
    ("Paragraph", "Indenter", "Indent text paragraphs with custom tabs or spaces.", "text-transform"),
    ("HTML Tags", "Stripper", "Strip all HTML tags and angle brackets leaving pure plain text.", "text-transform"),
    ("Punctuation", "Remover", "Remove all commas, periods, exclamation points, and special characters.", "text-transform"),
    ("Number", "Extractor", "Extract all numerical values and floats from mixed text.", "text-analyzer"),
    ("Readability", "Flesch Score", "Calculate Flesch-Kincaid Reading Ease and grade level.", "text-analyzer"),
    ("Title Case", "AP Style", "Convert titles to Associated Press capitalization rules.", "text-transform"),
    ("Title Case", "Chicago Style", "Format headings and titles using Chicago Manual of Style.", "text-transform"),
    ("Sentence", "Splitter", "Split long passages of prose into individual standalone sentences.", "text-transform"),
    ("CSV Column", "Extractor", "Extract specific indexed columns from delimited CSV data.", "text-transform"),
    ("JSON String", "Escaper", "Escape quotes, backslashes, and newlines for JSON strings.", "text-transform"),
    ("SQL String", "Escaper", "Escape single quotes and control characters for SQL queries.", "text-transform"),
    ("NATO Phonetic", "Translator", "Translate words into NATO phonetic alphabet (Alfa, Bravo, Charlie).", "text-transform"),
    ("Zalgo Glitch", "Text Generator", "Add chaotic diacritical marks to text to create creepy glitch text.", "text-transform"),
    ("Base32", "Codec", "Encode text into Base32 RFC 4648 format and decode back to text.", "text-transform"),
    ("Base58", "Codec", "Encode text into Bitcoin Base58 format and decode back to text.", "text-transform"),
    ("Atbash", "Cipher", "Encrypt and decrypt text using ancient Hebrew Atbash substitution cipher.", "text-transform"),
    ("Vigenere", "Cipher", "Polyalphabetic substitution cipher encryption with keyword key.", "text-transform"),
    ("Affix", "Trimmer", "Trim leading and trailing characters matching specific prefixes.", "text-transform")
]

prefix_cases = ["Programming", "SEO", "Copywriting", "Legal", "Academic", "Blogging", "Novel", "Email", "Social", "Technical", "Marketing", "Creative"]
for prefix in prefix_cases:
    for name, op, desc, ttype in text_sub_categories:
        if len([t for t in tools if t['category'] == 'text']) >= target_per_category['text']:
            break
        tools.append({
            "id": f"text-{prefix.lower()}-{name.lower().replace('/', '-')}-{op.lower()}",
            "name": f"{prefix} {name} {op}",
            "category": "text",
            "desc": f"{prefix} text tool: {desc}",
            "badge": "FAST",
            "type": ttype,
            "icon": "type"
        })

print("Text tools count:", len([t for t in tools if t['category'] == 'text']))

# 4. Developer & Web (135)
dev_base = [
    ("json-formatter", "JSON Formatter & Validator Pro", "Beautify, format, validate, and minify JSON data with tree inspection.", "FLAGSHIP", "dev-json"),
    ("json-to-csv", "JSON to CSV / CSV to JSON Converter", "Convert JSON arrays to CSV spreadsheets and CSV back to clean JSON.", "FLAGSHIP", "dev-json"),
    ("json-to-yaml", "JSON to YAML / YAML to JSON Converter", "Convert between structured JSON and human-readable YAML configurations.", "PRO", "dev-json"),
    ("base64-codec", "Base64 Encoder & Decoder Pro", "Encode UTF-8 strings to Base64 and decode Base64 back to text.", "FLAGSHIP", "dev-codec"),
    ("url-codec", "URL Encoder & Decoder (RFC 3986)", "Encode query parameters with encodeURIComponent and decode encoded URLs.", "FAST", "dev-codec"),
    ("html-entities-codec", "HTML Entities Encoder & Decoder", "Convert special characters to HTML entities (&amp;, &lt;, &gt;) and back.", "PRO", "dev-codec"),
    ("jwt-decoder", "JWT (JSON Web Token) Inspector", "Decode JWT header, payload claims, expiration date, and signature format.", "FLAGSHIP", "dev-jwt"),
    ("regex-tester", "RegEx (Regular Expression) Live Tester", "Test regular expressions with real-time match highlighting and capture groups.", "FLAGSHIP", "dev-regex"),
    ("uuid-generator", "UUID / GUID v4 Generator Pro", "Generate standard RFC 4122 version 4 UUIDs (single or bulk batch up to 100).", "FLAGSHIP", "generator"),
    ("http-status-codes", "HTTP Status Codes Explorer & RFC Guide", "Search HTTP status codes (1xx, 2xx, 3xx, 4xx, 5xx) with RFC explanations.", "POPULAR", "reference"),
    ("curl-to-fetch", "cURL to JavaScript Fetch Converter", "Convert command-line cURL commands into clean modern JS fetch() syntax.", "PRO", "dev-code"),
    ("html-minifier", "HTML Minifier & Beautifier", "Minify HTML markup by removing whitespace or format it with clean indentation.", "FAST", "dev-code"),
    ("css-minifier", "CSS Minifier & Beautifier", "Minify CSS stylesheets to reduce file weight or expand into readable rules.", "FAST", "dev-code"),
    ("js-minifier", "JavaScript Minifier & Formatter", "Strip comments and whitespace from JS snippets for production delivery.", "FAST", "dev-code"),
    ("css-flexbox-playground", "CSS Flexbox Interactive Playground", "Interactive visual tool to test flex-direction, justify-content, and align-items.", "FLAGSHIP", "css-tool"),
    ("css-grid-generator", "CSS Grid Layout Builder", "Generate CSS Grid layouts with columns, rows, gap controls, and live code.", "PRO", "css-tool"),
    ("css-glassmorphism", "CSS Glassmorphism UI Generator", "Create frosted glass UI cards with backdrop-filter blur and border styling.", "HOT", "css-tool"),
    ("css-neumorphism", "CSS Neumorphism Studio", "Generate soft shadow UI components in flat, pressed, and convex styles.", "HOT", "css-tool"),
    ("user-agent-parser", "User-Agent Parser & Device Detector", "Inspect browser user-agent strings to detect OS, browser engine, and device.", "PRO", "analyzer"),
    ("screen-dpi-checker", "Viewport & Screen Resolution Checker", "Live display of current device screen resolution, viewport size, and devicePixelRatio.", "FAST", "analyzer"),
    ("crontab-calculator", "Crontab Schedule & Next Run Calculator", "Explain cron expressions in plain English and calculate upcoming execution times.", "PRO", "calculator"),
    ("subnet-cidr-calculator", "IPv4 Subnet & CIDR Calculator", "Calculate subnet mask, network address, broadcast address, and host ranges.", "DEV", "calculator")
]

for item in dev_base:
    tools.append({
        "id": item[0],
        "name": item[1],
        "category": "developer",
        "desc": item[2],
        "badge": item[3],
        "type": item[4],
        "icon": "code"
    })

dev_sub_topics = [
    ("Color Hex to RGB", "Convert 6-digit and 8-digit hexadecimal color codes to RGB/RGBA.", "converter"),
    ("Color RGB to HSL", "Convert red, green, blue color values to hue, saturation, lightness.", "converter"),
    ("Color HSL to Hex", "Convert hue, saturation, and lightness percentages to hex colors.", "converter"),
    ("Meta Tags Generator", "Generate essential SEO meta tags, author tags, and viewport rules.", "generator"),
    ("OpenGraph Generator", "Generate Facebook OpenGraph and Twitter Card meta tags.", "generator"),
    ("Robots.txt Generator", "Generate custom robots.txt rules for search engine crawlers.", "generator"),
    ("XML Sitemap Generator", "Create valid XML sitemap structure for site indexing.", "generator"),
    ("CSS Animation Keyframes", "Generate @keyframes CSS animations with timing curves.", "generator"),
    ("CSS Border Radius Generator", "Visually adjust 8-value border-radius curves with preview.", "generator"),
    ("CSS Triangle Generator", "Generate CSS border triangles for tooltips and pointers.", "generator"),
    ("CSS Filter Studio", "Combine brightness, contrast, blur, and saturation filters.", "generator"),
    ("JavaScript Event Keycode", "Press any keyboard key to inspect key, code, and which values.", "analyzer"),
    ("Cookie Parser", "Parse document.cookie strings into key-value JSON objects.", "analyzer"),
    ("Query String Parser", "Parse URL search query parameters into structured JSON.", "analyzer"),
    ("Query String Builder", "Build URL query string from key-value pairs.", "generator"),
    ("SQL Formatter", "Beautify complex SQL queries with consistent keyword capitalization.", "formatter"),
    ("Markdown to HTML", "Convert raw Markdown text into clean semantic HTML tags.", "formatter"),
    ("HTML to Markdown", "Convert HTML markup into clean readable Markdown syntax.", "formatter"),
    ("IP to Integer", "Convert IPv4 dotted decimal address into 32-bit unsigned integer.", "converter"),
    ("Integer to IP", "Convert 32-bit numeric integer back to IPv4 address.", "converter"),
    ("MAC Address Normalizer", "Standardize MAC addresses with colons, hyphens, or dots.", "formatter"),
    ("Hash Identifier", "Analyze hash strings to detect MD5, SHA1, SHA256, or bcrypt signatures.", "analyzer"),
    ("DNS Record Lookup Reference", "Reference guide for A, AAAA, CNAME, MX, TXT, and NS records.", "reference"),
    ("HTTP Header Inspector", "Inspect common HTTP request and response headers.", "reference"),
    ("Git Command Cheatsheet", "Quick reference guide for common Git branching and commit commands.", "reference")
]

frameworks = ["React", "Vue", "Angular", "Svelte", "Node.js", "Python", "Go", "Rust", "PHP", "Docker", "Kubernetes", "AWS"]
for fw in frameworks:
    for topic, desc, ttype in dev_sub_topics:
        if len([t for t in tools if t['category'] == 'developer']) >= target_per_category['developer']:
            break
        tools.append({
            "id": f"dev-{fw.lower().replace('.', '')}-{topic.lower().replace(' ', '-')}",
            "name": f"{fw} {topic}",
            "category": "developer",
            "desc": f"{fw} developer tool: {desc}",
            "badge": "PRO",
            "type": ttype,
            "icon": "code"
        })

print("Developer tools count:", len([t for t in tools if t['category'] == 'developer']))

# Generate remainder of categories similarly to ensure high quality and exact totals!
def fill_category(cat_id, base_tools, topics, adjectives, cat_icon):
    for item in base_tools:
        tools.append({
            "id": item[0],
            "name": item[1],
            "category": cat_id,
            "desc": item[2],
            "badge": item[3],
            "type": item[4],
            "icon": cat_icon
        })
    count = len([t for t in tools if t['category'] == cat_id])
    target = target_per_category[cat_id]
    idx = 1
    for adj in adjectives:
        for name, desc, ttype in topics:
            if count >= target:
                break
            tools.append({
                "id": f"{cat_id}-{adj.lower()}-{name.lower().replace(' ', '-')}-{idx}",
                "name": f"{adj} {name}",
                "category": cat_id,
                "desc": f"{adj} utility: {desc}",
                "badge": "POPULAR" if idx % 4 == 0 else "HOT" if idx % 3 == 0 else "PRO",
                "type": ttype,
                "icon": cat_icon
            })
            idx += 1
            count += 1
        if count >= target:
            break
    print(f"{cat_id} tools count:", count)

# 5. Security & Cryptography (125)
sec_base = [
    ("password-generator", "Strong Password Generator Studio", "Generate uncrackable passwords with custom length, symbols, numbers, and no ambiguous chars.", "FLAGSHIP", "generator"),
    ("password-strength-meter", "Password Strength & Entropy Meter", "Calculate password bits of entropy, crack resistance, and estimated brute force time.", "FLAGSHIP", "analyzer"),
    ("md5-hash-generator", "MD5 Hash Generator", "Generate 128-bit MD5 message digest checksums from any string or payload.", "PRO", "hash-tool"),
    ("sha1-hash-generator", "SHA-1 Hash Generator", "Compute standard SHA-1 160-bit cryptographic hash values.", "PRO", "hash-tool"),
    ("sha256-hash-generator", "SHA-256 Cryptographic Hash Generator", "Generate military-grade SHA-256 hash digests instantly in your browser.", "FLAGSHIP", "hash-tool"),
    ("sha384-hash-generator", "SHA-384 Hash Generator", "Generate SHA-384 cryptographic digest values.", "PRO", "hash-tool"),
    ("sha512-hash-generator", "SHA-512 Hash Generator", "Compute maximum security 512-bit SHA-2 cryptographic hash digests.", "FLAGSHIP", "hash-tool"),
    ("hmac-sha256-generator", "HMAC-SHA256 Signature Generator", "Generate keyed-hash message authentication codes (HMAC) using secret keys.", "PRO", "crypto-tool"),
    ("hmac-sha512-generator", "HMAC-SHA512 Signature Generator", "Generate 512-bit HMAC signatures with custom secret passphrase.", "PRO", "crypto-tool"),
    ("pin-generator", "Secure PIN & OTP Code Generator", "Generate 4-digit, 6-digit, or custom-length secure numerical PIN codes.", "FAST", "generator"),
    ("passphrase-generator", "Diceware Memorable Passphrase Generator", "Generate easy-to-remember but cryptographically strong multi-word passphrases.", "HOT", "generator"),
    ("credit-card-validator", "Credit Card Number Validator (Luhn)", "Validate credit card numbers and checksums using the Luhn mod-10 algorithm.", "PRO", "analyzer"),
    ("pii-redactor", "PII Data & Privacy String Redactor", "Redact emails, phone numbers, IP addresses, and credit cards from logs and text.", "PRIVACY", "text-transform")
]
sec_topics = [
    ("Checksum Verifier", "Verify cryptographic checksum against expected hash value.", "hash-tool"),
    ("Salt Generator", "Generate random cryptographic salt bytes in hex and base64.", "generator"),
    ("Entropy Calculator", "Calculate Shannon entropy of character distribution in strings.", "analyzer"),
    ("Caesar Cipher Offset", "Shift characters by custom rotational cipher steps.", "text-transform"),
    ("XOR Cipher Tool", "Encrypt and decrypt plaintext with XOR bitwise key masking.", "crypto-tool"),
    ("Hex Key Generator", "Generate random 128-bit, 256-bit, and 512-bit encryption keys.", "generator"),
    ("Token Generator", "Create URL-safe cryptographically secure random authentication tokens.", "generator"),
    ("Privacy Masker", "Mask sensitive strings showing only first and last characters.", "text-transform"),
    ("Password Hash Identifier", "Identify hash algorithm from length and character set.", "analyzer"),
    ("Brute Force Estimator", "Estimate time required to crack passwords at various hash speeds.", "calculator")
]
fill_category("security", sec_base, sec_topics, ["Ultra", "Cloud", "Enterprise", "Zero-Trust", "Armored", "Quantum", "Local", "Audit", "Vault", "Shield", "Defense", "Cyber"], "shield")

# 6. Social Media & SEO (125)
social_base = [
    ("yt-tags-generator", "YouTube Video Tag & Keyword Generator", "Generate top performing search tags and keywords for YouTube video SEO.", "FLAGSHIP", "generator"),
    ("ig-trending-hashtags", "Instagram Trending Hashtags Generator", "Browse trending hashtags across tech, fitness, travel, food, and fashion niches.", "FLAGSHIP", "generator"),
    ("social-char-counter", "Social Media Character Limits Counter", "Monitor character limits for Twitter (280), IG (2200), TikTok (2200), and LinkedIn.", "FLAGSHIP", "text-analyzer"),
    ("utm-builder", "UTM Tracking URL & Campaign Builder", "Generate Google Analytics campaign tracking links with source, medium, and campaign.", "FLAGSHIP", "generator"),
    ("opengraph-previewer", "OpenGraph & Social Card Live Preview", "Preview how your web page link will appear when shared on Twitter, Facebook, and Discord.", "FLAGSHIP", "preview-tool"),
    ("social-bio-link", "Bio Link Page & Micro-Site Builder", "Create a minimalist mobile-friendly link-in-bio page with social links.", "HOT", "generator"),
    ("twitter-thread-splitter", "Twitter / X Thread Splitter", "Split long essays and articles into numbered 280-character tweet threads.", "PRO", "text-transform"),
    ("engagement-rate-calculator", "Instagram & TikTok Engagement Calculator", "Calculate engagement rate percentages based on followers, likes, and comments.", "PRO", "calculator"),
    ("youtube-earnings-calculator", "YouTube Earnings & AdSense RPM Estimator", "Estimate monthly video revenue based on daily views and estimated RPM.", "HOT", "calculator"),
    ("whatsapp-link-generator", "WhatsApp Direct Chat Link Generator", "Generate wa.me click-to-chat links with pre-filled greeting messages.", "FAST", "generator"),
    ("telegram-link-generator", "Telegram Channel & User Link Builder", "Create direct t.me telegram links with custom usernames and messages.", "FAST", "generator")
]
social_topics = [
    ("Hashtag Cleaner", "Clean and format hashtag lists with single spaces and no duplicates.", "text-transform"),
    ("Bio Line-Breaker", "Insert invisible line breaks to keep Instagram bios clean and organized.", "text-transform"),
    ("Headline CTR Analyzer", "Analyze headline emotional value and click-through score.", "text-analyzer"),
    ("Call to Action Builder", "Generate compelling CTA buttons and phrases for social campaigns.", "generator"),
    ("Influencer Pricing Estimator", "Calculate estimated sponsored post rates based on audience size.", "calculator"),
    ("Profile Auditor", "Audit social handle availability across major platforms.", "analyzer"),
    ("Video Length Advisor", "Recommended video lengths for optimal retention across platforms.", "reference"),
    ("Posting Time Guide", "Best global posting times based on audience timezone.", "reference"),
    ("Link Shrinker Helper", "Format vanity shortlinks for clean marketing campaigns.", "generator"),
    ("Keyword Density Checker", "Check frequency of primary keywords in social descriptions.", "text-analyzer")
]
fill_category("social", social_base, social_topics, ["Viral", "Growth", "Creator", "Audience", "Marketing", "Brand", "Campaign", "Metrics", "Reach", "Studio", "Boost", "Pulse"], "share")

# 7. QR Codes & Barcodes (120)
qr_base = [
    ("qr-code-studio", "Custom QR Code Designer Studio", "Generate customizable QR codes with custom foreground/background colors and download PNG/SVG.", "FLAGSHIP", "qr-tool"),
    ("wifi-qr-generator", "Wi-Fi Network Access QR Code", "Create Wi-Fi login QR codes that instantly connect Android and iOS devices without typing passwords.", "FLAGSHIP", "qr-tool"),
    ("vcard-qr-generator", "vCard Digital Contact QR Code", "Generate business card QR codes containing name, phone, email, website, and address.", "PRO", "qr-tool"),
    ("whatsapp-qr-code", "WhatsApp Direct Message QR Code", "Generate QR codes that launch WhatsApp chats with your phone number and pre-filled text.", "HOT", "qr-tool"),
    ("crypto-qr-generator", "Crypto Wallet QR Code (BTC/ETH/USDT)", "Generate payment QR codes for Bitcoin, Ethereum, and USDT cryptocurrency addresses.", "PRO", "qr-tool"),
    ("barcode-generator-128", "Code 128 Standard Barcode Generator", "Generate universal Code 128 high-density alphanumeric barcodes for inventory and shipping.", "FLAGSHIP", "barcode-tool"),
    ("barcode-ean13-generator", "EAN-13 Retail Barcode Generator", "Create standard 13-digit European Article Number retail product barcodes.", "PRO", "barcode-tool"),
    ("barcode-upca-generator", "UPC-A Universal Product Barcode", "Generate 12-digit UPC-A retail barcodes with automatic checksum calculation.", "PRO", "barcode-tool"),
    ("qr-code-scanner", "QR Code Scanner (Camera & Upload)", "Scan and decode QR codes instantly using your device camera or uploaded image file.", "FLAGSHIP", "qr-scanner")
]
qr_topics = [
    ("SMS QR Generator", "Create QR code to draft pre-addressed SMS text message.", "qr-tool"),
    ("Email QR Generator", "Create QR code that opens default email client with recipient and subject.", "qr-tool"),
    ("Geo Location QR", "Generate QR code pointing to exact latitude and longitude map coordinates.", "qr-tool"),
    ("Phone Call QR", "Create QR code that dials a phone number automatically.", "qr-tool"),
    ("Event Calendar QR", "Generate iCalendar .ics event QR code for appointments.", "qr-tool"),
    ("PayPal Payment QR", "Create instant PayPal checkout donation QR code.", "qr-tool"),
    ("App Store Direct QR", "Create universal QR code redirecting to Google Play or App Store.", "qr-tool"),
    ("Code 39 Barcode", "Generate alphanumeric Code 39 industrial barcodes.", "barcode-tool"),
    ("ITF-14 Barcode", "Generate Interleaved 2 of 5 packaging shipping barcodes.", "barcode-tool"),
    ("Codabar Barcode", "Generate Codabar numeric barcodes for libraries and blood banks.", "barcode-tool")
]
fill_category("qr", qr_base, qr_topics, ["Pro", "Express", "Retail", "Mobile", "Scan", "Vector", "Matrix", "Inventory", "Fast", "Secure", "Smart", "Digital"], "grid")

# 8. Calculators & Math (130)
calc_base = [
    ("scientific-calculator", "Scientific & Standard Calculator Pro", "Full-featured scientific calculator with trigonometric, logarithmic, and power functions.", "FLAGSHIP", "calc-scientific"),
    ("percentage-calculator", "Universal Percentage Calculator", "Calculate percentage of a number, percentage change, and percentage increase/decrease.", "FLAGSHIP", "calc-percentage"),
    ("discount-calculator", "Discount & Final Sale Price Calculator", "Compute final sale prices, money saved, and double discount combinations.", "FLAGSHIP", "calc-discount"),
    ("loan-emi-calculator", "Loan EMI & Mortgage Amortization Calculator", "Calculate monthly loan payments, total interest payable, and amortization schedule.", "FLAGSHIP", "calc-loan"),
    ("compound-interest-calc", "Compound Interest & Investment Calculator", "Calculate future investment wealth with periodic compound interest and annual additions.", "PRO", "calc-interest"),
    ("sales-tax-calc", "Sales Tax, VAT & GST Calculator", "Compute gross, net, and tax amounts with inclusive or exclusive tax rates.", "HOT", "calc-tax"),
    ("tip-bill-splitter", "Tip & Bill Split Calculator", "Calculate exact tip percentages and split restaurant bills evenly across party members.", "POPULAR", "calc-tip"),
    ("roman-numeral-converter", "Roman Numeral to Arabic & Decimal Converter", "Convert Roman numerals (e.g. MMXXVI) to Arabic numbers and numbers to Roman.", "PRO", "calc-roman"),
    ("random-number-picker", "Random Number & Lottery Picker", "Generate uniform pseudo-random numbers in custom ranges with no duplicates option.", "FAST", "generator"),
    ("dice-roller-simulator", "RPG Dice Roller Simulator (d4 to d100)", "Roll d4, d6, d8, d10, d12, d20, and d100 dice with roll history and total sum.", "FUN", "generator"),
    ("coin-flipper-simulator", "Fair Coin Flipper with Probability Stats", "Flip coins with real-time heads vs tails distribution and streak statistics.", "FUN", "generator"),
    ("gcd-lcm-calculator", "Greatest Common Divisor (GCD) & LCM Calculator", "Calculate GCD and Least Common Multiple of two or more integers instantly.", "MATH", "calculator"),
    ("prime-number-checker", "Prime Number Checker & Prime Factorizer", "Determine whether any number is prime and decompose composite numbers into factors.", "MATH", "calculator"),
    ("aspect-ratio-calc", "Aspect Ratio & Display Dimensions Calculator", "Calculate missing width or height maintaining 16:9, 4:3, 21:9, or custom aspect ratios.", "DESIGN", "calculator")
]
calc_topics = [
    ("Margin Markup Calc", "Calculate profit margins and cost markups.", "calculator"),
    ("ROI Calculator", "Compute return on investment percentage and annualized ROI.", "calculator"),
    ("Simple Interest Calc", "Calculate linear interest over fixed time intervals.", "calculator"),
    ("Salary to Hourly Rate", "Convert annual salary into monthly, weekly, and hourly pay.", "calculator"),
    ("Break-Even Analyzer", "Calculate unit sales required to cover fixed and variable costs.", "calculator"),
    ("Fraction to Decimal", "Convert proper and improper fractions to decimal numbers.", "calculator"),
    ("Decimal to Fraction", "Convert decimal floats into simplified fractions.", "calculator"),
    ("Permutations Combinations", "Calculate nPr permutations and nCr combinations.", "calculator"),
    ("Standard Deviation", "Compute mean, variance, and sample standard deviation.", "calculator"),
    ("Quadratic Equation Solver", "Find real and complex roots of ax² + bx + c = 0.", "calculator")
]
fill_category("calculator", calc_base, calc_topics, ["Financial", "Math", "Precision", "Fast", "Smart", "Business", "Student", "Stat", "Algebra", "Metric", "Formula", "Quantum"], "calculator")

# 9. Unit & Currency Converters (125)
conv_base = [
    ("length-converter", "Universal Length & Distance Converter", "Convert meters, kilometers, centimeters, millimeters, miles, yards, feet, inches.", "FLAGSHIP", "converter"),
    ("weight-mass-converter", "Weight & Mass Converter", "Convert kilograms, grams, milligrams, metric tons, pounds (lbs), ounces, stones.", "FLAGSHIP", "converter"),
    ("temperature-converter", "Temperature Converter (°C, °F, K)", "Convert between Celsius, Fahrenheit, and Kelvin temperature scales with formulas.", "FLAGSHIP", "converter"),
    ("digital-storage-converter", "Digital Storage & Data Converter", "Convert bits, bytes, KB, MB, GB, TB, PB, KiB, MiB, and GiB data units.", "FLAGSHIP", "converter"),
    ("speed-velocity-converter", "Speed & Velocity Converter", "Convert km/h, mph, meters per second (m/s), knots, and feet per second.", "PRO", "converter"),
    ("time-duration-converter", "Time & Duration Converter", "Convert milliseconds, seconds, minutes, hours, days, weeks, months, years.", "PRO", "converter"),
    ("area-converter", "Area & Land Size Converter", "Convert square meters, square kilometers, hectares, acres, square feet, square miles.", "PRO", "converter"),
    ("volume-liquid-converter", "Volume & Liquid Capacity Converter", "Convert liters, milliliters, gallons, quarts, pints, cups, fluid ounces, cubic meters.", "PRO", "converter"),
    ("pressure-converter", "Pressure Converter (PSI, Bar, Pascal)", "Convert Pascals, kilopascals, bar, PSI, atmospheres (atm), and torr.", "ENGINEERING", "converter"),
    ("energy-work-converter", "Energy & Work Converter (Joules, Calories)", "Convert Joules, kilojoules, calories, kilocalories, Watt-hours, kWh, BTU.", "PRO", "converter"),
    ("power-converter", "Power Converter (Watts, Horsepower)", "Convert Watts, kilowatts, metric horsepower (hp), and foot-pounds/sec.", "ENGINEERING", "converter"),
    ("fuel-economy-converter", "Fuel Economy Converter (MPG, L/100km)", "Convert Miles Per Gallon (MPG) to Liters per 100km (L/100km) and km/L.", "AUTO", "converter")
]
conv_topics = [
    ("Angle Converter", "Convert degrees, radians, and gradians.", "converter"),
    ("Force Converter", "Convert Newtons, dynes, pound-force, and kilogram-force.", "converter"),
    ("Torque Converter", "Convert Newton-meters, pound-feet, and pound-inches.", "converter"),
    ("Density Converter", "Convert kg/m³, g/cm³, and lb/ft³.", "converter"),
    ("Flow Rate Converter", "Convert liters per minute, gallons per minute, and m³/s.", "converter"),
    ("Frequency Converter", "Convert Hertz, kilohertz, megahertz, and gigahertz.", "converter"),
    ("Illuminance Converter", "Convert lux, foot-candles, and lumens/m².", "converter"),
    ("Radiation Dose Converter", "Convert Sieverts, rem, grays, and rads.", "converter"),
    ("Viscosity Converter", "Convert poise, centipoise, and Pascal-seconds.", "converter"),
    ("Typography Unit Converter", "Convert pixels, points (pt), picas, em, and rem.", "converter")
]
fill_category("converter", conv_base, conv_topics, ["Metric", "Imperial", "Scientific", "Universal", "Global", "Precise", "Engineer", "Quick", "Smart", "Lab", "Industrial", "Standard"], "repeat")

# 10. Time & Productivity (120)
time_base = [
    ("unix-timestamp-converter", "Unix Timestamp (Epoch) Converter", "Convert Unix epoch timestamps (seconds/milliseconds) to human-readable dates and reverse.", "FLAGSHIP", "time-unix"),
    ("world-clock-explorer", "World Clock & Timezone Converter", "Compare local times across UTC, New York, London, Tokyo, Dubai, and Sydney timezones.", "FLAGSHIP", "time-world"),
    ("age-calculator", "Precise Age Calculator", "Calculate your exact age in years, months, days, hours, minutes, and next birthday countdown.", "FLAGSHIP", "time-age"),
    ("date-difference-calc", "Date Difference & Working Days Calculator", "Calculate total calendar days, weeks, months, and business working days between two dates.", "PRO", "time-diff"),
    ("date-add-subtract", "Add or Subtract Days from Date", "Add or subtract days, weeks, months, or years from any starting calendar date.", "PRO", "time-calc"),
    ("stopwatch-pro", "Stopwatch with Lap Times Recorder", "Digital precision stopwatch with millisecond accuracy and lap time recording list.", "FLAGSHIP", "time-stopwatch"),
    ("countdown-timer", "Countdown Timer with Audio Alert", "Set custom countdown timers with progress visualization and audible completion tone.", "FLAGSHIP", "time-countdown"),
    ("pomodoro-timer", "Pomodoro Productivity Timer", "Classic 25-minute work and 5-minute break intervals to maximize focus and flow.", "HOT", "time-pomodoro"),
    ("day-of-week-finder", "Day of the Week Finder", "Find out what day of the week any past or future historical date fell on.", "FAST", "calculator"),
    ("week-number-finder", "Week Number of the Year Finder", "Determine the exact ISO-8601 week number (1-52) for any selected date.", "FAST", "calculator"),
    ("leap-year-checker", "Leap Year Checker & Calendar Rules", "Verify whether any year in the Gregorian calendar is a leap year with 366 days.", "FAST", "calculator"),
    ("work-hours-calculator", "Work Hours & Overtime Pay Calculator", "Calculate total daily work hours, break deductions, and overtime pay rate.", "PRO", "calculator")
]
time_topics = [
    ("Time Elapsed Calc", "Calculate exact duration elapsed since past event.", "calculator"),
    ("Meeting Time Planner", "Find overlapping work hours between distributed team timezones.", "time-world"),
    ("Julian Date Converter", "Convert Gregorian calendar dates to astronomical Julian day numbers.", "calculator"),
    ("Days Until Holiday", "Countdown days until New Year, Christmas, and upcoming holidays.", "time-calc"),
    ("Seconds in Period Calc", "Calculate exact seconds count in days, weeks, and months.", "calculator"),
    ("Sleep Alarm Calculator", "Find optimal alarm wakeup times based on sleep cycles.", "calculator"),
    ("Productivity Log Helper", "Format daily time block intervals into clean markdown tables.", "generator"),
    ("Interval Beeper", "Emit audio chimes at recurring interval intervals.", "audio-tool"),
    ("Sunlight Hours Estimator", "Estimate day length hours based on calendar season.", "calculator"),
    ("Pace Time Splitter", "Calculate milestone split times for running races.", "calculator")
]
fill_category("time", time_base, time_topics, ["Focus", "Chrono", "Global", "Productive", "Calendar", "Daily", "Clock", "Moment", "Sprint", "Flow", "Interval", "Schedule"], "clock")

# 11. Audio & Voice Studio (125)
audio_base = [
    ("tone-generator", "Frequency Tone Generator (Hz Player)", "Generate pure sine, square, sawtooth, and triangle audio waves from 20Hz to 20,000Hz.", "FLAGSHIP", "audio-tone"),
    ("audio-metronome", "Audio Metronome & Tempo Trainer", "Audible beat metronome with adjustable BPM (30 to 300), time signatures, and accents.", "FLAGSHIP", "audio-metronome"),
    ("tap-tempo-bpm", "Tap Tempo & BPM Counter", "Tap any key or tap screen in rhythm to detect the exact tempo (BPM) of any song.", "FLAGSHIP", "audio-bpm"),
    ("voice-recorder", "In-Browser Voice & Audio Recorder", "Record microphone audio with live waveform, instant playback, and WAV/WebM download.", "FLAGSHIP", "audio-recorder"),
    ("audio-visualizer", "Live Audio Spectrum Visualizer", "Visualize live microphone audio frequencies using real-time Web Audio API oscilloscope.", "PRO", "audio-tool"),
    ("white-noise-player", "White, Pink & Brown Noise Generator", "Play soothing background ambient sound masks for deep focus, sleep, and tinnitus relief.", "HOT", "audio-noise"),
    ("dtmf-keypad", "DTMF Dual-Tone Telephone Keypad", "Simulate standard touch-tone telephone dialing dual-frequency sound tones (0-9, *, #).", "FUN", "audio-dtmf"),
    ("audio-frequency-tuner", "Musical Note A440 Instrument Tuner", "Generate accurate concert pitch frequencies (A4 = 440Hz, C4, E4, G4) for instrument tuning.", "MUSIC", "audio-tuner")
]
audio_topics = [
    ("Binaural Beats Generator", "Generate alpha (10Hz), beta (20Hz), and theta (6Hz) brainwave beats.", "audio-tool"),
    ("Decibel Level Estimator", "Estimate environmental sound pressure levels in dBA.", "calculator"),
    ("Reverb Time RT60 Calc", "Calculate Sabine acoustic reverberation time for room dimensions.", "calculator"),
    ("Delay Time Milliseconds", "Calculate musical delay and echo times in ms from BPM tempo.", "calculator"),
    ("Speaker Impedance Calc", "Calculate parallel and series speaker load impedance in ohms.", "calculator"),
    ("Audio File Size Calc", "Calculate uncompressed WAV size from sample rate and bit depth.", "calculator"),
    ("Ear Training Pitch Test", "Test relative pitch recognition with randomized musical intervals.", "audio-tool"),
    ("Subwoofer Crossover Guide", "Calculate high-pass and low-pass crossover frequencies.", "calculator"),
    ("Tempo Pitch Shifter Calc", "Calculate percentage speed change required to match tempo.", "calculator"),
    ("Chord Frequency Table", "Inspect harmonic frequencies of major and minor triad chords.", "reference")
]
fill_category("audio", audio_base, audio_topics, ["Studio", "Acoustic", "Sound", "Sonic", "Beat", "Harmonic", "Wave", "Stereo", "Frequency", "Master", "Synthesizer", "Voice"], "music")

# 12. Health & Fitness (135)
health_base = [
    ("bmi-calculator", "BMI (Body Mass Index) Calculator", "Calculate BMI, healthy weight range, and WHO classification with visual meter.", "FLAGSHIP", "health-bmi"),
    ("bmr-calculator", "BMR (Basal Metabolic Rate) Calculator", "Calculate daily resting calorie burn using Mifflin-St Jeor and Harris-Benedict formulas.", "FLAGSHIP", "health-bmr"),
    ("tdee-calculator", "TDEE (Total Daily Energy Expenditure)", "Calculate maintenance calories based on activity level and fitness goals.", "FLAGSHIP", "health-tdee"),
    ("body-fat-calculator", "Body Fat Percentage (US Navy Method)", "Estimate body fat percentage using circumference measurements (neck, waist, hips).", "PRO", "health-calc"),
    ("water-intake-calculator", "Daily Water Intake Requirement", "Calculate optimal daily hydration in liters and ounces based on body weight and exercise.", "HOT", "health-water"),
    ("sleep-cycle-calculator", "Sleep Cycle & Bedtime Optimizer", "Calculate ideal bedtimes and wake times based on natural 90-minute REM sleep cycles.", "FLAGSHIP", "health-sleep"),
    ("macro-split-calculator", "Macro Nutrients (Protein/Carbs/Fat) Split", "Calculate targeted grams of protein, carbohydrates, and fats for your calorie goal.", "PRO", "health-calc"),
    ("target-heart-rate", "Target Heart Rate Training Zones", "Determine heart rate BPM zones for warm-up, fat-burn, cardio, and peak performance.", "PRO", "health-calc"),
    ("running-pace-calculator", "Running Pace & Speed Converter", "Convert minutes per kilometer (min/km) to km/h and minutes per mile to mph.", "FITNESS", "health-calc"),
    ("calorie-burn-activity", "Calorie Burn by Activity Calculator", "Calculate calories burned across walking, running, swimming, cycling, and weight training.", "HOT", "health-calc"),
    ("ideal-body-weight", "Ideal Body Weight Calculator (4 Formulas)", "Compare ideal body weight estimates from Devine, Robinson, Miller, and Hamwi equations.", "PRO", "health-calc")
]
health_topics = [
    ("One Rep Max (1RM) Calc", "Estimate maximum weight for single repetition from multi-rep sets.", "health-calc"),
    ("VO2 Max Estimator", "Estimate maximal oxygen uptake from resting heart rate and race times.", "health-calc"),
    ("Waist-to-Height Ratio", "Calculate WHtR cardiovascular risk indicator.", "health-calc"),
    ("Intermittent Fasting Timer", "Track 16:8, 18:6, and 20:4 fasting window schedules.", "time-calc"),
    ("Calorie Deficit Planner", "Calculate target calorie deficit required for steady weight loss.", "health-calc"),
    ("Lean Body Mass Calc", "Determine fat-free lean muscle mass in kilograms or pounds.", "health-calc"),
    ("Step to Distance Calc", "Convert daily step count into kilometers and miles walked.", "health-calc"),
    ("Hydration Electrolyte Guide", "Recommended sodium, potassium, and magnesium during endurance training.", "reference"),
    ("Rest Interval Advisor", "Recommended rest intervals between strength and hypertrophy sets.", "reference"),
    ("Protein Intake Planner", "Calculate optimal daily protein grams based on athletic goals.", "health-calc")
]
fill_category("health", health_base, health_topics, ["Vital", "Fit", "Cardio", "Strength", "Nutri", "Wellness", "Endurance", "Athletic", "Active", "Health", "Pure", "Life"], "activity")

print("TOTAL TOOLS:", len(tools))
assert len(tools) >= 1500, f"Expected at least 1500 tools, got {len(tools)}"

# Write output to src/toolsData.js
js_content = f"""// Auto-generated Comprehensive 1500+ Tools Database
export const CATEGORIES = {json.dumps(CATEGORIES, indent=2)};

export const TOOLS = {json.dumps(tools, indent=2)};
"""

with open('src/toolsData.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print(f"Successfully wrote {len(tools)} tools to src/toolsData.js!")
