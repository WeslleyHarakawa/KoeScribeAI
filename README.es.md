<div align="center">

**🌐 Leer en otro idioma:**&nbsp;&nbsp;
[🇺🇸 English](README.md) &nbsp;|&nbsp; [🇧🇷 Português](README.pt.md) &nbsp;|&nbsp; 🇪🇸 Español &nbsp;|&nbsp; [🇯🇵 日本語](README.ja.md) &nbsp;|&nbsp; [🇳🇱 Nederlands](README.nl.md)

---

# 🎤 KoeScribe AI

**Widget Flotante de Voz a Texto con IA para Windows · macOS · Linux**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Open Source](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-red)](https://github.com/WeslleyHarakawa/KoeScribeAI)
[![Gratis](https://img.shields.io/badge/Gratis-100%25-brightgreen)](https://github.com/WeslleyHarakawa/KoeScribeAI)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue?logo=python)](https://python.org)
[![PyQt6](https://img.shields.io/badge/UI-PyQt6-41CD52?logo=qt)](https://pypi.org/project/PyQt6/)
[![Powered by Groq](https://img.shields.io/badge/Powered%20by-Groq%20Whisper-F55036)](https://groq.com)

<br/>

> *"KoeScribe" viene de 声 (Koe) — que significa "voz" en japonés — y Scribe, que significa escribir.*
> *Una voz que escribe por ti, en cualquier lugar de tu pantalla.*

<br/>

[![Buy Me A Coffee](https://img.shields.io/badge/☕%20Invítame%20un%20Café-Apoya%20este%20proyecto-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/weslleyaharakawa)
&nbsp;
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Weslley%20Harakawa-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/weslleyharakawa/)

</div>

---

## ✨ ¿Qué es KoeScribe AI?

KoeScribe AI es un widget flotante **gratuito y de código abierto** que permanece siempre encima de todas tus ventanas y transcribe tu voz en **tiempo real**, escribiendo el texto directamente en cualquier aplicación donde esté tu cursor — como un dictado nativo, pero con IA de vanguardia.

Sin suscripciones. Sin complicaciones. Solo habla y las palabras aparecen. 🚀

---

## 🎯 Características

- 🎤 **Transcripción en tiempo real** — habla y escribe al mismo tiempo mientras tú hablas
- 🖥️ **Widget flotante siempre visible** — visible sobre cualquier app (Word, Chrome, VS Code, Slack...)
- 🌐 **13 idiomas de transcripción** — Portugués, Inglés, Español, Japonés, Chino, Francés, Alemán, Italiano, Holandés, Ruso y más
- 🗣️ **6 idiomas de interfaz** — English, Português, Español, 日本語, 中文, Nederlands
- ⚡ **Múltiples proveedores de IA** — Groq (¡nivel gratuito!), OpenAI Whisper, Anthropic
- 💾 **Guarda tu configuración** — clave API y preferencias se recuerdan
- 🖱️ **Arrastrable y minimalista** — diseño oscuro compacto tipo glassmorphism
- 🔔 **Bandeja del sistema** — minimiza a la bandeja y accede desde la barra de tareas
- ❓ **Ayuda integrada** — guía paso a paso para obtener tu clave API
- ☕ **Buy Me a Coffee** — apoya al desarrollador directamente desde la app

---

## 🚀 Cómo empezar

### Opción 1 — Descargar el ejecutable (¡sin necesidad de Python!)

Ve a [**Releases**](https://github.com/WeslleyHarakawa/KoeScribeAI/releases) y descarga la versión correcta para tu PC:

| Archivo | Arquitectura |
|------|-------------|
| `KoeScribe_AI_ARM64.exe` | Windows ARM (Snapdragon, Surface Pro X...) |
| `KoeScribe_AI_Intel_AMD_x64.exe` | Windows Intel / AMD (la mayoría de PCs) |

¡Solo doble clic y listo — sin instalación!

### Opción 2 — Ejecutar desde el código fuente

```bash
# 1. Clona el repositorio
git clone https://github.com/WeslleyHarakawa/KoeScribeAI.git
cd KoeScribeAI

# 2. Crea un entorno virtual
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # macOS / Linux

# 3. Instala las dependencias
pip install -r requirements.txt

# 4. ¡Ejecuta!
python app.py
```

---

## 🔑 Cómo obtener tu clave API gratuita

KoeScribe AI usa proveedores de IA para la transcripción. La forma más fácil de empezar es con **Groq** — completamente gratis:

1. Ve a [console.groq.com](https://console.groq.com) y crea una cuenta
2. Haz clic en **API Keys** → **Create API Key**
3. Copia la clave
4. Abre KoeScribe AI → haz clic en **⚙️** → pega tu clave → **Guardar**

> 💡 El nivel gratuito de Groq es muy generoso — perfecto para uso personal diario.

---

## 🌍 Idiomas soportados

### Transcripción (voz → texto)
| Idioma | Código |
|---|---|
| Portugués (Brasil) | pt-BR |
| Portugués (Portugal) | pt-PT |
| Inglés (EE.UU.) | en-US |
| Inglés (Británico) | en-GB |
| Español (Latinoamérica) | es |
| Español (España) | es-ES |
| Japonés | ja |
| Chino | zh |
| Francés | fr |
| Alemán | de |
| Italiano | it |
| Holandés | nl |
| Ruso | ru |

### Idiomas de la interfaz
English · Português · Español · 日本語 · 中文 · Nederlands

---

## 🔧 Compilar desde el código fuente

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

## 🤝 Contribuir

Este proyecto es **gratuito y de código abierto** — hecho para la comunidad, por la comunidad ❤️

¡Los pull requests son bienvenidos! Siéntete libre de:
- Agregar nuevos idiomas de interfaz
- Agregar nuevos proveedores de transcripción
- Mejorar la interfaz
- Corregir errores

Por favor abre un issue antes de hacer cambios importantes.

---

## 📄 Licencia

Este proyecto está bajo la **Licencia MIT** — libre de usar, modificar y distribuir.
Consulta [LICENSE](LICENSE) para más detalles.

---

<div align="center">

Desarrollado por [Weslley Harakawa](https://github.com/WeslleyHarakawa) usando [Antigravity AI](https://antigravity.dev)

[![Buy Me A Coffee](https://img.shields.io/badge/☕-Invítame%20un%20café-FFDD00?style=flat-square)](https://buymeacoffee.com/weslleyaharakawa)
&nbsp;
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Conectar-0A66C2?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/weslleyharakawa/)
&nbsp;
[![GitHub](https://img.shields.io/badge/GitHub-Seguir-181717?style=flat-square&logo=github)](https://github.com/WeslleyHarakawa)

*¡Si KoeScribe AI te ahorró tiempo, considera invitarme un café — eso mantiene vivo este proyecto! ☕*

</div>
