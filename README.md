# Niji Local

**Niji Local** is a clean, ChatGPT-inspired chat workspace that runs at **`http://127.0.0.1:12076`** and talks only to a model server on the same device. It is built for Android/Termux and Windows, works well on small screens, and has no account, analytics, cloud database, or runtime dependencies.

> The address is `127.0.0.1:12076` — not `120:76:00`. `127.0.0.1` means “this device only.”

![License: MIT](https://img.shields.io/badge/license-MIT-b8ef63.svg)
![Node 18+](https://img.shields.io/badge/node-18%2B-9ba99e.svg)

## What it does

- **Local-first chat:** conversation history, model settings, theme, and system instructions are kept in browser storage on your device.
- **No cloud proxy:** the included server accepts only `localhost`, `127.0.0.1`, or IPv6 loopback model endpoints. It will refuse LAN and internet URLs.
- **Two local server types:** [Ollama](https://ollama.com/) native API and OpenAI-compatible servers such as `llama-server` / llama.cpp or LM Studio.
- **Proper mobile UI:** responsive drawer, touch-friendly controls, safe-area spacing, streaming replies, stop generation, chat rename/delete, and local import/export.
- **Low-resource defaults:** Eco mode caps replies at 384 tokens. Turn it off only when you need longer output.
- **Your instructions:** set your own system prompt. This interface does not add content filtering or send a transcript to a remote moderation service; the behavior of the model itself depends on the model you choose.

## Quick start — Windows

1. Install **Node.js 18+**.
2. Download/clone this repository and open its folder.
3. Double-click `scripts\setup-windows.bat` once.
4. Start your local model server (examples below).
5. Double-click `scripts\start-windows.bat`.
6. Open **http://127.0.0.1:12076**, select **Settings**, find/select a downloaded model, and save.

The batch launcher deliberately binds the UI to `127.0.0.1`, so it is not exposed on your Wi-Fi network.

## Quick start — Android with Termux

> A phone needs enough RAM/storage for the model you choose. A small quantized 1B–3B GGUF model is a practical starting point. Keep the screen awake and use a charger for long generations.

1. Install [Termux from F-Droid or GitHub](https://termux.dev/en/) (avoid the obsolete Play Store build).
2. In Termux, install the tools:

   ```sh
   pkg update && pkg upgrade
   pkg install git nodejs-lts
   ```

3. Clone this repository, then set up the UI:

   ```sh
   git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
   cd YOUR-REPOSITORY
   bash scripts/setup-termux.sh
   ```

4. Run a **local** inference server in Termux or another on-device app. Then, in a second Termux session:

   ```sh
   bash scripts/start-termux.sh
   ```

5. In your Android browser, visit **http://127.0.0.1:12076**. In **Settings**, use the address and provider that match your local model server.

If the browser cannot connect, make sure both the model server and Niji Local are still running, and use `127.0.0.1` rather than `localhost`.

## Connect a model

Niji Local is the interface, not a bundled model. Start one model engine first, then use **Settings → Find models**.

### Ollama (desktop / supported environments)

```sh
ollama pull llama3.2:3b
ollama serve
```

Use **Provider: Ollama**, address `http://127.0.0.1:11434`, and model `llama3.2:3b`.

### llama.cpp / `llama-server` (good fit for a local GGUF model)

Launch your installed `llama-server` with a GGUF model. The exact binary and package installation vary by operating system; a typical command is:

```sh
./llama-server -m /path/to/your-model.gguf --host 127.0.0.1 --port 8080
```

Use **Provider: OpenAI-compatible**, address `http://127.0.0.1:8080/v1`, then click **Find models**. Some builds expose the model ID automatically; otherwise type the model ID shown by that server.

### LM Studio (Windows)

Start its local server with the OpenAI-compatible API enabled. Use its displayed local address (commonly `http://127.0.0.1:1234/v1`) and select **OpenAI-compatible**.

## Privacy and local-data controls

- Press **Settings → Export chats** before clearing browser data or changing phones.
- **Import backup** restores chats and local settings from an exported JSON file.
- **Clear all** irreversibly removes Niji Local’s browser storage for this origin.
- This repository makes no analytics, telemetry, tracking, or external-font requests. The only model request route is the loopback address you enter.
- The model engine is a separate program and has its own behavior, performance, and license. Follow applicable law, model licenses, and the consent/privacy rights of people whose data you process.

## Development

```sh
npm install
npm start       # http://127.0.0.1:12076
npm test
npm run check
```

There is no production build step: the Node server serves the static interface directly. For development auto-reload of the server process, use `npm run dev`.

## Architecture

```text
Browser UI (history in localStorage)
       │ POST /api/chat, /api/models
       ▼
Niji Local server — 127.0.0.1:12076
       │ validates loopback-only destination
       ├── Ollama — 127.0.0.1:11434/api/…
       └── OpenAI-compatible — 127.0.0.1:8080/v1/…
```

The small proxy avoids CORS configuration and streams output to the browser. It deliberately has no account system and does not persist message content on the server.

## License

MIT. See [LICENSE](LICENSE).
