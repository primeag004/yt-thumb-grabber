#!/data/data/com.termux/files/usr/bin/bash
# One-time Niji Local setup for Termux. This script only installs this UI;
# install/download a model using the local inference engine of your choice.
set -euo pipefail

if ! command -v node >/dev/null 2>&1; then
  echo "Node.js was not found. In Termux, run: pkg install nodejs-lts"
  exit 1
fi

NODE_MAJOR="$(node -p "process.versions.node.split('.')[0]")"
if [ "$NODE_MAJOR" -lt 18 ]; then
  echo "Node.js 18 or newer is required (found $(node --version))."
  exit 1
fi

echo "Installing Niji Local (no telemetry, no runtime dependencies)…"
npm install --no-audit --no-fund
chmod +x scripts/start-termux.sh
echo
echo "Done. Start the UI with: bash scripts/start-termux.sh"
echo "Then open: http://127.0.0.1:12076"
