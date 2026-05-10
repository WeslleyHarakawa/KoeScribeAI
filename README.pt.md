<div align="center">

**🌐 Leia em outro idioma:**&nbsp;&nbsp;
[🇺🇸 English](README.md) &nbsp;|&nbsp; 🇧🇷 Português &nbsp;|&nbsp; [🇪🇸 Español](README.es.md) &nbsp;|&nbsp; [🇯🇵 日本語](README.ja.md)

---

# 🎤 KoeScribe AI

**Widget Flutuante de Transcrição de Voz com IA para Windows · macOS · Linux**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Open Source](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-red)](https://github.com/WeslleyHarakawa/KoeScribeAI)
[![Gratuito](https://img.shields.io/badge/Gratuito-100%25-brightgreen)](https://github.com/WeslleyHarakawa/KoeScribeAI)
[![Feito com Python](https://img.shields.io/badge/Feito%20com-Python-blue?logo=python)](https://python.org)
[![PyQt6](https://img.shields.io/badge/UI-PyQt6-41CD52?logo=qt)](https://pypi.org/project/PyQt6/)
[![Powered by Groq](https://img.shields.io/badge/Powered%20by-Groq%20Whisper-F55036)](https://groq.com)

<br/>

> *"KoeScribe" vem de 声 (Koe) — que significa "voz" em japonês — e Scribe, que significa escrever.*
> *Uma voz que escreve por você, em qualquer lugar da sua tela.*

<br/>

[![Buy Me A Coffee](https://img.shields.io/badge/☕%20Me%20pague%20um%20Café-Apoie%20este%20projeto-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/weslleyaharakawa)
&nbsp;
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Weslley%20Harakawa-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/weslleyharakawa/)

</div>

---

## ✨ O que é o KoeScribe AI?

O KoeScribe AI é um widget flutuante **gratuito e open source** que fica sempre sobre todas as suas janelas e transcreve sua voz em **tempo real**, digitando o texto diretamente no aplicativo onde o cursor estiver — como um ditado nativo, mas com inteligência artificial de ponta.

Sem assinatura. Sem complicação. É só falar que as palavras aparecem. 🚀

---

## 🎯 Funcionalidades

- 🎤 **Transcrição em tempo real** — fala e digita ao mesmo tempo enquanto você fala
- 🖥️ **Widget flutuante sempre visível** — fica sobre qualquer app (Word, Chrome, VS Code, Slack...)
- 🌐 **13 idiomas de transcrição** — Português, Inglês, Espanhol, Japonês, Chinês, Francês, Alemão, Italiano, Holandês, Russo e mais
- 🗣️ **6 idiomas de interface** — English, Português, Español, 日本語, 中文, Nederlands
- ⚡ **Múltiplos provedores de IA** — Groq (plano gratuito!), OpenAI Whisper, Anthropic
- 💾 **Salva suas configurações** — chave API e preferências são lembradas
- 🖱️ **Arrastável e minimalista** — design escuro e compacto estilo glassmorphism
- 🔔 **Bandeja do sistema** — minimize para a bandeja e acesse pelo relógio do Windows
- ❓ **Ajuda integrada** — guia passo a passo para obter sua chave API
- ☕ **Buy Me a Coffee** — apoie o desenvolvedor diretamente pelo app

---

## 🚀 Como usar

### Opção 1 — Baixar o executável (sem precisar de Python!)

Vá em [**Releases**](https://github.com/WeslleyHarakawa/KoeScribeAI/releases) e baixe a versão certa para o seu PC:

| Arquivo | Arquitetura |
|------|-------------|
| `KoeScribe_AI_ARM64.exe` | Windows ARM (Snapdragon, Surface Pro X...) |
| `KoeScribe_AI_Intel_AMD_x64.exe` | Windows Intel / AMD (maioria dos PCs) |

Só dar dois cliques e rodar — sem instalar nada!

### Opção 2 — Rodar pelo código-fonte

```bash
# 1. Clone o repositório
git clone https://github.com/WeslleyHarakawa/KoeScribeAI.git
cd KoeScribeAI

# 2. Crie um ambiente virtual
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # macOS / Linux

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Execute!
python app.py
```

---

## 🔑 Como obter sua chave API gratuita

O KoeScribe AI usa provedores de IA para transcrição. A forma mais fácil de começar é com o **Groq** — é completamente gratuito:

1. Acesse [console.groq.com](https://console.groq.com) e crie uma conta
2. Clique em **API Keys** → **Create API Key**
3. Copie a chave
4. Abra o KoeScribe AI → clique em **⚙️** → cole sua chave → **Salvar**

> 💡 O plano gratuito do Groq é muito generoso — perfeito para uso pessoal diário.

---

## 🌍 Idiomas suportados

### Transcrição (voz → texto)
| Idioma | Código |
|---|---|
| Português (Brasil) | pt-BR |
| Português (Portugal) | pt-PT |
| Inglês (EUA) | en-US |
| Inglês (Britânico) | en-GB |
| Espanhol (América Latina) | es |
| Espanhol (Espanha) | es-ES |
| Japonês | ja |
| Chinês | zh |
| Francês | fr |
| Alemão | de |
| Italiano | it |
| Holandês | nl |
| Russo | ru |

### Idiomas da interface
English · Português · Español · 日本語 · 中文 · Nederlands

---

## 🔧 Compilar a partir do código-fonte

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

## 🤝 Contribuindo

Este projeto é **gratuito e open source** — feito para a comunidade, pela comunidade ❤️

Pull requests são bem-vindos! Sinta-se à vontade para:
- Adicionar novos idiomas de interface
- Adicionar novos provedores de transcrição
- Melhorar a interface
- Corrigir bugs

Por favor, abra uma issue antes de fazer mudanças grandes.

---

## 📄 Licença

Este projeto está licenciado sob a **Licença MIT** — livre para usar, modificar e distribuir.
Veja [LICENSE](LICENSE) para detalhes.

---

<div align="center">

Desenvolvido por [Weslley Harakawa](https://github.com/WeslleyHarakawa) usando [Antigravity AI](https://antigravity.dev)

[![Buy Me A Coffee](https://img.shields.io/badge/☕-Me%20pague%20um%20café-FFDD00?style=flat-square)](https://buymeacoffee.com/weslleyaharakawa)
&nbsp;
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Conectar-0A66C2?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/weslleyharakawa/)
&nbsp;
[![GitHub](https://img.shields.io/badge/GitHub-Seguir-181717?style=flat-square&logo=github)](https://github.com/WeslleyHarakawa)

*Se o KoeScribe AI te ajudou, considere me pagar um café — isso mantém o projeto vivo! ☕*

</div>
