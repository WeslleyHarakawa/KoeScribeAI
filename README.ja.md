<div align="center">

**🌐 他の言語で読む:**&nbsp;&nbsp;
[🇺🇸 English](README.md) &nbsp;|&nbsp; [🇧🇷 Português](README.pt.md) &nbsp;|&nbsp; 🇯🇵 日本語 &nbsp;|&nbsp; [🇳🇱 Nederlands](README.nl.md)

---

# 🎤 KoeScribe AI

**Windows · macOS · Linux 向け 浮動AIボイスメモウィジェット**

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Open Source](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-red)](https://github.com/WeslleyHarakawa/KoeScribeAI)
[![無料で使える](https://img.shields.io/badge/%E7%84%A1%E6%96%99-100%25-brightgreen)](https://github.com/WeslleyHarakawa/KoeScribeAI)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue?logo=python)](https://python.org)
[![PyQt6](https://img.shields.io/badge/UI-PyQt6-41CD52?logo=qt)](https://pypi.org/project/PyQt6/)
[![Powered by Groq](https://img.shields.io/badge/Powered%20by-Groq%20Whisper-F55036)](https://groq.com)

<br/>

> *「KoeScribe」は、日本語で「声」を意味する 声（Koe）と、書くことを意味する Scribe を組み合わせた名前です。*
> *あなたのために、画面上のどこでも書いてくれる声。*

<br/>

[![Buy Me A Coffee](https://img.shields.io/badge/☕%20コーヒーをおごる-このプロジェクトを応援-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/weslleyaharakawa)
&nbsp;
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Weslley%20Harakawa-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/weslleyharakawa/)

</div>

---

## ✨ KoeScribe AI とは？

KoeScribe AI は**無料でオープンソース**の浮動ウィジェットです。すべてのウィンドウの上に常に表示され、声をリアルタイムで文字起こしして、カーソルがある場所に直接テキストを入力します。まるでネイティブの音声入力のように、最先端のAIを使って動作します。

サブスクリプション不要。複雑な設定不要。話すだけで文字が現れます。🚀

---

## 🎯 機能

- 🎤 **リアルタイム文字起こし** — 話しながら同時に入力
- 🖥️ **常に最前面に表示** — Word、Chrome、VS Code、Slackなど、どのアプリの上にも表示
- 🌐 **13の文字起こし言語** — ポルトガル語、英語、スペイン語、日本語、中国語、フランス語、ドイツ語、イタリア語、オランダ語、ロシア語など
- 🗣️ **6つのインターフェース言語** — English、Português、Español、日本語、中文、Nederlands
- ⚡ **複数のAIプロバイダー** — Groq（無料枠あり！）、OpenAI Whisper、Anthropic
- 💾 **設定を保存** — APIキーと設定が記憶される
- 🖱️ **ドラッグ可能でコンパクト** — ダークなグラスモーフィズムデザイン
- 🔔 **システムトレイ対応** — トレイに最小化してタスクバーからアクセス
- ❓ **組み込みヘルプ** — APIキー取得の手順ガイド付き
- ☕ **Buy Me a Coffee** — アプリから直接開発者を応援

---

## 🚀 はじめ方

### オプション1 — 実行ファイルをダウンロード（Pythonは不要！）

[**Releases**](https://github.com/WeslleyHarakawa/KoeScribeAI/releases) でお使いのPCに合ったバージョンをダウンロードしてください：

| ファイル | アーキテクチャ |
|------|-------------|
| `KoeScribe_AI_ARM64.exe` | Windows ARM（Snapdragon、Surface Pro Xなど） |
| `KoeScribe_AI_Intel_AMD_x64.exe` | Windows Intel / AMD（ほとんどのPC） |

ダブルクリックで起動 — インストール不要！

### オプション2 — ソースコードから実行

```bash
# 1. リポジトリをクローン
git clone https://github.com/WeslleyHarakawa/KoeScribeAI.git
cd KoeScribeAI

# 2. 仮想環境を作成
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # macOS / Linux

# 3. 依存関係をインストール
pip install -r requirements.txt

# 4. 実行！
python app.py
```

---

## 🔑 無料APIキーの取得方法

KoeScribe AIはAIプロバイダーを使って文字起こしします。最も簡単に始める方法は**Groq** — 完全無料です：

1. [console.groq.com](https://console.groq.com) にアクセスしてアカウントを作成
2. **API Keys** → **Create API Key** をクリック
3. キーをコピー
4. KoeScribe AIを開く → **⚙️** をクリック → キーを貼り付け → **保存**

> 💡 Groqの無料枠は非常に寛大です — 日常的な個人使用に最適です。

---

## 🌍 対応言語

### 文字起こし（音声→テキスト）
| 言語 | コード |
|---|---|
| ポルトガル語（ブラジル） | pt-BR |
| ポルトガル語（ポルトガル） | pt-PT |
| 英語（アメリカ） | en-US |
| 英語（イギリス） | en-GB |
| スペイン語（ラテンアメリカ） | es |
| スペイン語（スペイン） | es-ES |
| 日本語 | ja |
| 中国語 | zh |
| フランス語 | fr |
| ドイツ語 | de |
| イタリア語 | it |
| オランダ語 | nl |
| ロシア語 | ru |

### インターフェース言語
English · Português · Español · 日本語 · 中文 · Nederlands

---

## 🤝 コントリビュート

このプロジェクトは**無料でオープンソース** — コミュニティのためにコミュニティが作りました ❤️

プルリクエスト歓迎！
- 新しいインターフェース言語の追加
- 新しい文字起こしプロバイダーの追加
- UIの改善
- バグ修正

大きな変更の前にIssueを作成してください。

---

## 📄 ライセンス

このプロジェクトは**MITライセンス**の下でライセンスされています — 自由に使用、修正、配布できます。
詳細は [LICENSE](LICENSE) をご覧ください。

---

<div align="center">

[Weslley Harakawa](https://github.com/WeslleyHarakawa) が [Antigravity AI](https://antigravity.dev) を使って開発

[![Buy Me A Coffee](https://img.shields.io/badge/☕-コーヒーをおごる-FFDD00?style=flat-square)](https://buymeacoffee.com/weslleyaharakawa)
&nbsp;
[![LinkedIn](https://img.shields.io/badge/LinkedIn-つながる-0A66C2?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/weslleyharakawa/)
&nbsp;
[![GitHub](https://img.shields.io/badge/GitHub-フォロー-181717?style=flat-square&logo=github)](https://github.com/WeslleyHarakawa)

*KoeScribe AI が役に立ったなら、コーヒーをおごってください — このプロジェクトを続ける力になります！ ☕*

</div>
