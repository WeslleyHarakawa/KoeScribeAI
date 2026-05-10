<div align="center">

**🌐 Lees in jouw taal:**&nbsp;&nbsp;
[🇺🇸 English](README.md) &nbsp;|&nbsp; [🇧🇷 Português](README.pt.md) &nbsp;|&nbsp; [🇯🇵 日本語](README.ja.md) &nbsp;|&nbsp; 🇳🇱 Nederlands

---

# 🎤 KoeScribe AI

**Zwevende AI Spraak-naar-Tekst Widget voor Windows · macOS · Linux**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Open Source](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-red)](https://github.com/WeslleyHarakawa/KoeScribeAI)
[![Gratis te gebruiken](https://img.shields.io/badge/Gratis-100%25-brightgreen)](https://github.com/WeslleyHarakawa/KoeScribeAI)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue?logo=python)](https://python.org)
[![PyQt6](https://img.shields.io/badge/UI-PyQt6-41CD52?logo=qt)](https://pypi.org/project/PyQt6/)
[![Powered by Groq](https://img.shields.io/badge/Powered%20by-Groq%20Whisper-F55036)](https://groq.com)

<br/>

> *"KoeScribe" komt van 声 (Koe) — Japans voor "stem" — en Scribe, wat schrijven betekent.*
> *Een stem die voor jou schrijft, overal op je scherm.*

<br/>

[![Buy Me A Coffee](https://img.shields.io/badge/☕%20Trakteer%20me%20op%20Koffie-Steun%20dit%20project-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/weslleyaharakawa)
&nbsp;
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Weslley%20Harakawa-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/weslleyharakawa/)

</div>

---

## ✨ Wat is KoeScribe AI?

KoeScribe AI is een **gratis, open-source** zwevende widget die altijd boven al je vensters zichtbaar blijft en je stem **in realtime** omzet naar tekst — direct getypt in elke applicatie waar je cursor staat. Zoals een native dicteertool, maar aangedreven door geavanceerde AI.

Geen abonnement. Geen gedoe. Gewoon spreken en de woorden verschijnen. 🚀

---

## 🎯 Functies

- 🎤 **Realtime transcriptie** — spreekt en typt tegelijkertijd terwijl jij praat
- 🖥️ **Altijd-bovenop zwevende widget** — zichtbaar boven elk programma (Word, Chrome, VS Code, Slack...)
- 🌐 **13 transcriptietalen** — Portugees, Engels, Spaans, Japans, Chinees, Frans, Duits, Italiaans, Nederlands, Russisch en meer
- 🗣️ **6 interfacetalen** — English, Português, Español, 日本語, 中文, Nederlands
- ⚡ **Meerdere AI-providers** — Groq (gratis tier!), OpenAI Whisper, Anthropic
- 💾 **Instellingen worden opgeslagen** — API-sleutel en voorkeuren worden onthouden
- 🖱️ **Versleepbaar & minimalistisch** — compact, donker glassmorphism-ontwerp
- 🔔 **Systeemvak** — minimaliseer naar het systeemvak, toegankelijk via de taakbalk
- ❓ **Ingebouwde hulp** — stap-voor-stap gids om je API-sleutel te verkrijgen
- ☕ **Buy Me a Coffee** — ondersteun de ontwikkelaar direct vanuit de app

---

## 🚀 Aan de slag

### Optie 1 — Download de uitvoerbare versie (geen Python nodig!)

Ga naar [**Releases**](https://github.com/WeslleyHarakawa/KoeScribeAI/releases) en download de juiste versie voor jouw pc:

| Bestand | Architectuur |
|------|-------------|
| `KoeScribe_AI_ARM64.exe` | Windows ARM (Snapdragon, Surface Pro X...) |
| `KoeScribe_AI_Intel_AMD_x64.exe` | Windows Intel / AMD (de meeste pc's) |

Gewoon dubbelklikken en starten — geen installatie nodig!

### Optie 2 — Uitvoeren vanuit broncode

```bash
# 1. Kloon de repository
git clone https://github.com/WeslleyHarakawa/KoeScribeAI.git
cd KoeScribeAI

# 2. Maak een virtuele omgeving aan
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # macOS / Linux

# 3. Installeer afhankelijkheden
pip install -r requirements.txt

# 4. Starten!
python app.py
```

---

## 🔑 Je gratis API-sleutel ophalen

KoeScribe AI gebruikt AI-providers voor transcriptie. De eenvoudigste manier om te beginnen is met **Groq** — volledig gratis:

1. Ga naar [console.groq.com](https://console.groq.com) en maak een account aan
2. Klik op **API Keys** → **Create API Key**
3. Kopieer de sleutel
4. Open KoeScribe AI → klik op **⚙️** → plak je sleutel → **Opslaan**

> 💡 Groq's gratis tier is zeer royaal — perfect voor dagelijks persoonlijk gebruik.

---

## 🌍 Ondersteunde talen

### Transcriptie (spraak → tekst)
| Taal | Code |
|---|---|
| Portugees (Brazilië) | pt-BR |
| Portugees (Portugal) | pt-PT |
| Engels (VS) | en-US |
| Engels (Brits) | en-GB |
| Spaans (Latijns-Amerika) | es |
| Spaans (Spanje) | es-ES |
| Japans | ja |
| Chinees | zh |
| Frans | fr |
| Duits | de |
| Italiaans | it |
| Nederlands | nl |
| Russisch | ru |

### Interfacetalen
English · Português · Español · 日本語 · 中文 · Nederlands

---

## 🤝 Bijdragen

Dit project is **gratis en open source** — gemaakt voor de gemeenschap, door de gemeenschap ❤️

Pull requests zijn welkom! Voel je vrij om:
- Nieuwe interfacetalen toe te voegen
- Nieuwe transcriptieproviders toe te voegen
- De UI te verbeteren
- Bugs te repareren

Open eerst een issue voordat je grote wijzigingen maakt.

---

## 📄 Licentie

Dit project is gelicenseerd onder de **MIT-licentie** — vrij te gebruiken, aan te passen en te distribueren.
Zie [LICENSE](LICENSE) voor details.

---

<div align="center">

Gebouwd door [Weslley Harakawa](https://github.com/WeslleyHarakawa) met behulp van [Antigravity AI](https://antigravity.dev)

[![Buy Me A Coffee](https://img.shields.io/badge/☕-Trakteer%20me%20op%20koffie-FFDD00?style=flat-square)](https://buymeacoffee.com/weslleyaharakawa)
&nbsp;
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Verbinden-0A66C2?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/weslleyharakawa/)
&nbsp;
[![GitHub](https://img.shields.io/badge/GitHub-Volgen-181717?style=flat-square&logo=github)](https://github.com/WeslleyHarakawa)

*Als KoeScribe AI je tijd heeft bespaard, overweeg dan om me op een koffie te trakteren — het houdt dit project in leven! ☕*

</div>
