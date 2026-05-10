<div align="center">

**🌐 Read in your language:**&nbsp;&nbsp;
🇺🇸 English &nbsp;|&nbsp; [🇧🇷 Português](README.pt.md) &nbsp;|&nbsp; [🇪🇸 Español](README.es.md) &nbsp;|&nbsp; [🇯🇵 日本語](README.ja.md) &nbsp;|&nbsp; [🇳🇱 Nederlands](README.nl.md)

---

# 🎤 KoeScribe AI

**Floating AI Voice-to-Text Widget for Windows · macOS · Linux**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Open Source](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-red)](https://github.com/WeslleyHarakawa/KoeScribeAI)
[![Free to Use](https://img.shields.io/badge/Free%20to%20Use-100%25-brightgreen)](https://github.com/WeslleyHarakawa/KoeScribeAI)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue?logo=python)](https://python.org)
[![PyQt6](https://img.shields.io/badge/UI-PyQt6-41CD52?logo=qt)](https://pypi.org/project/PyQt6/)
[![Powered by Groq](https://img.shields.io/badge/Powered%20by-Groq%20Whisper-F55036)](https://groq.com)

<br/>

> *"KoeScribe" comes from 声 (Koe) — Japanese for "voice" — and Scribe, meaning to write.*
> *A voice that writes for you, anywhere on your screen.*

<br/>

[![Buy Me A Coffee](https://img.shields.io/badge/☕%20Buy%20Me%20a%20Coffee-Support%20this%20project-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/weslleyaharakawa)
&nbsp;
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Weslley%20Harakawa-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/weslleyharakawa/)

</div>

---

## ✨ What is KoeScribe AI?

KoeScribe AI is a **free, open-source** floating widget that stays on top of all your windows and transcribes your voice in **real time**, typing the text directly into any application where your cursor is — just like a native dictation tool, but powered by state-of-the-art AI.

No subscriptions. No bloat. Just speak, and the words appear. 🚀

---

## 🎯 Features

- 🎤 **Real-time transcription** — speaks and types simultaneously as you talk
- 🖥️ **Always-on-top floating widget** — stays visible over any app (Word, Chrome, VS Code, Slack...)
- 🌐 **13 transcription languages** — Portuguese, English, Spanish, Japanese, Chinese, French, German, Italian, Dutch, Russian and more
- 🗣️ **6 interface languages** — English, Português, Español, 日本語, 中文, Nederlands
- ⚡ **Multiple AI providers** — Groq (free tier!), OpenAI Whisper, Anthropic
- 💾 **Saves your settings** — API key and preferences are remembered
- 🖱️ **Draggable & minimal** — tiny footprint, glass-dark design
- 🔔 **System tray** — minimize to tray, access from taskbar
- ❓ **Built-in help** — step-by-step guide to get your API key
- ☕ **Buy Me a Coffee** — support the dev directly from the app

---

## 🚀 Quick Start

### Option 1 — Download the executable (no Python needed!)

Go to [**Releases**](https://github.com/WeslleyHarakawa/KoeScribeAI/releases) and download the right version for your PC:

| File | Architecture |
|------|-------------|
| `KoeScribe_AI_ARM64.exe` | Windows on ARM (Snapdragon, Surface Pro X...) |
| `KoeScribe_AI_Intel_AMD_x64.exe` | Windows on Intel / AMD (most PCs) |

Just double-click and run — no installation needed!

### Option 2 — Run from source

```bash
# 1. Clone the repo
git clone https://github.com/WeslleyHarakawa/KoeScribeAI.git
cd KoeScribeAI

# 2. Create a virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # macOS / Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run!
python app.py
```

---

## 🔑 Getting your free API key

KoeScribe AI uses AI providers for transcription. The easiest way to get started is with **Groq** — it's completely free:

1. Go to [console.groq.com](https://console.groq.com) and create an account
2. Click **API Keys** → **Create API Key**
3. Copy the key
4. Open KoeScribe AI → click **⚙️** → paste your key → **Save**

> 💡 Groq's free tier is extremely generous — perfect for daily personal use.

---

## 🌍 Supported Languages

### Transcription (voice → text)
| Language | Code |
|---|---|
| Portuguese (Brazil) | pt-BR |
| Portuguese (Portugal) | pt-PT |
| English (USA) | en-US |
| English (British) | en-GB |
| Spanish (Latin America) | es |
| Spanish (Spain) | es-ES |
| Japanese | ja |
| Chinese | zh |
| French | fr |
| German | de |
| Italian | it |
| Dutch | nl |
| Russian | ru |

### Interface UI languages
English · Português · Español · 日本語 · 中文 · Nederlands

---

## 🔧 Build from Source

### Windows (ARM64)
```powershell
pip install pyinstaller
pyinstaller --onefile --windowed --name "KoeScribe AI" app.py
```

### Windows (Intel/AMD x64)
```powershell
pyinstaller --onefile --windowed --name "KoeScribe AI" app.py
```

### macOS
```bash
chmod +x build_mac.sh && ./build_mac.sh
```

### Linux (Ubuntu)
```bash
chmod +x build_linux.sh && ./build_linux.sh
```

---

## 🤝 Contributing

This project is **free and open source** — built for the community, by the community ❤️

Pull requests are welcome! Feel free to:
- Add new interface languages
- Add new transcription providers
- Improve the UI
- Fix bugs

Please open an issue first to discuss major changes.

---

## 📄 License

This project is licensed under the **MIT License** — free to use, modify and distribute.
See [LICENSE](LICENSE) for details.

---

<div align="center">

Built by [Weslley Harakawa](https://github.com/WeslleyHarakawa) using [Antigravity AI](https://antigravity.dev)

[![Buy Me A Coffee](https://img.shields.io/badge/☕-Buy%20me%20a%20coffee-FFDD00?style=flat-square)](https://buymeacoffee.com/weslleyaharakawa)
&nbsp;
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/weslleyharakawa/)
&nbsp;
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=flat-square&logo=github)](https://github.com/WeslleyHarakawa)

*If KoeScribe AI saved you time, consider buying me a coffee — it keeps this project alive! ☕*

</div>

