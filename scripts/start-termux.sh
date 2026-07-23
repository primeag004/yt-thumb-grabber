#!/data/data/com.termux/files/usr/bin/bash
# Keep this terminal open while using Niji Local.
set -euo pipefail
cd "$(dirname "$0")/.."
HOST=127.0.0.1 PORT=12076 npm start
