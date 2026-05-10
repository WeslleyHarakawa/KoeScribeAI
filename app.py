import sys
import threading
import tempfile
import os
import queue
import json
import webbrowser
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QFrame, QComboBox, QLineEdit, QSystemTrayIcon, QMenu
from PyQt6.QtCore import Qt, QPoint, pyqtSignal, QObject
from PyQt6.QtGui import QIcon, QFont, QColor, QPixmap, QPainter
import sounddevice as sd
import wave
import struct
import numpy as np
import keyboard

TRANSLATIONS = {
    "English": {
        "title": "KoeScribe AI Settings",
        "engine": "Transcription Engine:",
        "key": "API Key:",
        "key_ph": "Paste your API key here",
        "ui_lang": "Interface Language:",
        "audio_lang": "Transcription Language:",
        "save": "Save"
    },
    "Portuguese": {
        "title": "Configurações KoeScribe AI",
        "engine": "Motor de Transcrição:",
        "key": "Chave API:",
        "key_ph": "Cole sua chave da API aqui",
        "ui_lang": "Idioma da Interface:",
        "audio_lang": "Idioma da Transcrição:",
        "save": "Salvar"
    },
    "Spanish": {
        "title": "Configuraciones KoeScribe AI",
        "engine": "Motor de Transcripción:",
        "key": "Clave API:",
        "key_ph": "Pega tu clave de API aquí",
        "ui_lang": "Idioma de Interfaz:",
        "audio_lang": "Idioma de Transcripción:",
        "save": "Guardar"
    },
    "Japanese": {
        "title": "KoeScribe AI 設定",
        "engine": "文字起こしエンジン:",
        "key": "APIキー:",
        "key_ph": "ここにAPIキーを貼り付けます",
        "ui_lang": "インターフェース言語:",
        "audio_lang": "文字起こし言語:",
        "save": "保存"
    },
    "Chinese": {
        "title": "KoeScribe AI 设置",
        "engine": "转录引擎:",
        "key": "API 密钥:",
        "key_ph": "在此处粘贴您的 API 密钥",
        "ui_lang": "界面语言:",
        "audio_lang": "转录语言:",
        "save": "保存"
    },
    "Dutch": {
        "title": "KoeScribe AI Instellingen",
        "engine": "Transcriptie-engine:",
        "key": "API-sleutel:",
        "key_ph": "Plak hier uw API-sleutel",
        "ui_lang": "Interfacetaal:",
        "audio_lang": "Transcriptietaal:",
        "save": "Opslaan"
    }
}

# Internal keys (stored in config)
AUDIO_LANG_KEYS = [
    "Portuguese (Brazil)",
    "Portuguese (Portugal)",
    "English (USA)",
    "English (British)",
    "Spanish (Latin America)",
    "Spanish (Spain)",
    "Japanese",
    "Chinese",
    "French",
    "German",
    "Italian",
    "Dutch",
    "Russian"
]

# Display names per UI language
AUDIO_LANG_DISPLAY = {
    "English":    ["Portuguese (Brazil)", "Portuguese (Portugal)", "English (USA)", "English (British)", "Spanish (Latin America)", "Spanish (Spain)", "Japanese", "Chinese", "French", "German", "Italian", "Dutch", "Russian"],
    "Portuguese": ["Português (Brasil)", "Português (Portugal)", "Inglês (EUA)", "Inglês (Britânico)", "Espanhol (América Latina)", "Espanhol (Espanha)", "Japonês", "Chinês", "Francês", "Alemão", "Italiano", "Holandês", "Russo"],
    "Spanish":    ["Portugués (Brasil)", "Portugués (Portugal)", "Inglés (EE.UU.)", "Inglés (Británico)", "Español (Latinoamérica)", "Español (España)", "Japonés", "Chino", "Francés", "Alemán", "Italiano", "Holandés", "Ruso"],
    "Japanese":   ["ポルトガル語（ブラジル）", "ポルトガル語（ポルトガル）", "英語（アメリカ）", "英語（イギリス）", "スペイン語（ラテンアメリカ）", "スペイン語（スペイン）", "日本語", "中国語", "フランス語", "ドイツ語", "イタリア語", "オランダ語", "ロシア語"],
    "Chinese":    ["葡萄牙语（巴西）", "葡萄牙语（葡萄牙）", "英语（美国）", "英语（英国）", "西班牙语（拉丁美洲）", "西班牙语（西班牙）", "日语", "中文", "法语", "德语", "意大利语", "荷兰语", "俄语"],
    "Dutch":      ["Portugees (Brazilië)", "Portugees (Portugal)", "Engels (VS)", "Engels (Brits)", "Spaans (Latijns-Amerika)", "Spaans (Spanje)", "Japans", "Chinees", "Frans", "Duits", "Italiaans", "Nederlands", "Russisch"]
}

UI_LANG_KEYS = ["English", "Portuguese", "Spanish", "Japanese", "Chinese", "Dutch"]
UI_LANG_DISPLAY = {
    "English":    ["English",   "Portuguese", "Spanish",   "Japanese", "Chinese", "Dutch"],
    "Portuguese": ["Inglês",    "Português",  "Espanhol",  "Japonês",  "Chinês",  "Holandês"],
    "Spanish":    ["Inglés",    "Portugués",  "Español",   "Japonés",  "Chino",   "Holandés"],
    "Japanese":   ["英語",      "ポルトガル語", "スペイン語", "日本語",   "中国語",  "オランダ語"],
    "Chinese":    ["英语",      "葡萄牙语",   "西班牙语",  "日语",     "中文",   "荷兰语"],
    "Dutch":      ["Engels",    "Portugees",  "Spaans",    "Japans",   "Chinees", "Nederlands"],
}

HELP_TRANSLATIONS = {
    "English": {
        "title": "💳 LLM Credits & API Keys",
        "intro": "To use KoeScribe AI you need an <b style='color:white'>API key</b> from a transcription provider. Each provider gives you a <b style='color:white'>free credit</b> to start with.",
        "groq_desc": "Fastest & generous free tier.",
        "openai_desc": "Pay-as-you-go, ~$0.006/min.",
        "anthropic_desc": "Advanced AI, pay-as-you-go.",
        "steps": "1. Create account<br>2. Go to API Keys<br>3. Create key<br>4. Paste here."
    },
    "Portuguese": {
        "title": "💳 Créditos LLM & Chaves API",
        "intro": "Para usar o KoeScribe AI você precisa de uma <b style='color:white'>chave API</b> de um provedor de transcrição. Cada provedor oferece um <b style='color:white'>crédito gratuito</b> para começar.",
        "groq_desc": "Mais rápido e com tier gratuito generoso.",
        "openai_desc": "Pay-as-you-go, ~$0,006/min.",
        "anthropic_desc": "IA avançada, pay-as-you-go.",
        "steps": "1. Crie uma conta<br>2. Vá em API Keys<br>3. Crie a chave<br>4. Cole aqui."
    },
    "Spanish": {
        "title": "💳 Créditos LLM y Claves API",
        "intro": "Para usar KoeScribe AI necesitas una <b style='color:white'>clave API</b> de un proveedor de transcripción. Cada proveedor ofrece un <b style='color:white'>crédito gratuito</b> para empezar.",
        "groq_desc": "El más rápido y con tier gratuito generoso.",
        "openai_desc": "Pay-as-you-go, ~$0.006/min.",
        "anthropic_desc": "IA avanzada, pay-as-you-go.",
        "steps": "1. Crea una cuenta<br>2. Ve a API Keys<br>3. Crea la clave<br>4. Pégala aquí."
    },
    "Japanese": {
        "title": "💳 LLMクレジット & APIキー",
        "intro": "KoeScribe AIを使用するには、文字起こしプロバイダーからの<b style='color:white'>APIキー</b>が必要です。各プロバイダーは<b style='color:white'>無料クレジット</b>を提供しています。",
        "groq_desc": "最速・届出しの無料枠。",
        "openai_desc": "従量課金、約$0.006/分。",
        "anthropic_desc": "高度なAI、従量課金。",
        "steps": "1. アカウント作成<br>2. API Keysへ<br>3. キー作成<br>4. ここに貼り付け。"
    },
    "Chinese": {
        "title": "💳 LLM信用额和 API 密酐",
        "intro": "使用 KoeScribe AI 需要来自转录提供商的<b style='color:white'>API 密酐</b>。每个提供商都提供<b style='color:white'>免费信用额</b>。",
        "groq_desc": "最快且免费额度慢慢。",
        "openai_desc": "按用量计费，~$0.006/分钟。",
        "anthropic_desc": "高级 AI，按用量计费。",
        "steps": "1. 创建账号<br>2. 转到 API Keys<br>3. 创建密酐<br>4. 粘贴到这里。"
    },
    "Dutch": {
        "title": "💳 LLM-credits & API-sleutels",
        "intro": "Om KoeScribe AI te gebruiken heb je een <b style='color:white'>API-sleutel</b> nodig van een transcriptieprovider. Elke provider geeft je een <b style='color:white'>gratis tegoed</b> om mee te beginnen.",
        "groq_desc": "Snelste & royaal gratis niveau.",
        "openai_desc": "Betaal-per-gebruik, ~$0,006/min.",
        "anthropic_desc": "Geavanceerde AI, betaal-per-gebruik.",
        "steps": "1. Account aanmaken<br>2. Ga naar API Keys<br>3. Maak sleutel aan<br>4. Plak hier."
    }
}

class WorkerSignals(QObject):
    realtime_update = pyqtSignal(str)
    finished = pyqtSignal()
    error = pyqtSignal(str)

class RecorderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.load_config()
        self.is_recording = False
        self.is_processing = False
        self.audio_data = []
        self.samplerate = 16000
        self.stream = None
        self.signals = WorkerSignals()
        self.signals.realtime_update.connect(self.on_realtime_update)
        self.signals.finished.connect(self.on_finished)
        self.signals.error.connect(self.on_error)

        self.initUI()
        self.initTray()
        self.apply_translation()

    def load_config(self):
        self.config_path = os.path.join(os.path.expanduser("~"), ".transcritor_config.json")
        self.config = {
            "provider": "Groq", 
            "keys": {"Groq": "", "OpenAI": "", "Anthropic": ""}, 
            "language": "Portuguese (Brazil)",
            "ui_language": "English"
        }
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r") as f:
                    loaded_config = json.load(f)
                    self.config.update(loaded_config)
            except:
                pass
        
        if "language" not in self.config:
            self.config["language"] = "Portuguese (Brazil)"
        if "ui_language" not in self.config:
            self.config["ui_language"] = "English"
        
        # Key is loaded from config file if previously saved

    def save_config(self):
        provider = self.provider_combo.currentText()
        key = self.key_input.text()
        ui_lang = self.ui_lang_combo.currentData()  # internal key e.g. "Portuguese"
        
        # Convert displayed (sorted) lang index back to internal key
        display_idx = self.lang_combo.currentIndex()
        sorted_keys = getattr(self, '_sorted_lang_keys', AUDIO_LANG_KEYS)
        lang_key = sorted_keys[display_idx] if 0 <= display_idx < len(sorted_keys) else "Portuguese (Brazil)"
        
        self.config["provider"] = provider
        self.config["language"] = lang_key
        self.config["ui_language"] = ui_lang
        if key:
            self.config["keys"][provider] = key
        with open(self.config_path, "w") as f:
            json.dump(self.config, f)
            
        self.apply_translation()
        self.toggle_settings()

    def apply_translation(self):
        ui_lang = self.config.get("ui_language", "English")
        if ui_lang not in TRANSLATIONS:
            ui_lang = "English"
        
        t = TRANSLATIONS[ui_lang]
        self.title_lbl.setText(t["title"])
        self.provider_lbl.setText(t["engine"])
        self.key_lbl.setText(t["key"])
        self.key_input.setPlaceholderText(t["key_ph"])
        self.ui_lang_lbl.setText(t["ui_lang"])
        self.lang_lbl.setText(t["audio_lang"])
        self.save_btn.setText(t["save"])
        
        # Rebuild lang_combo sorted alphabetically by display name
        current_key = AUDIO_LANG_KEYS[self.lang_combo.currentIndex()] if self.lang_combo.currentIndex() >= 0 else self.config.get("language", "Portuguese (Brazil)")
        display_names = AUDIO_LANG_DISPLAY.get(ui_lang, AUDIO_LANG_DISPLAY["English"])
        sorted_pairs = sorted(zip(display_names, AUDIO_LANG_KEYS), key=lambda x: x[0].lower())
        self.lang_combo.blockSignals(True)
        self.lang_combo.clear()
        self._sorted_lang_keys = [k for _, k in sorted_pairs]
        self.lang_combo.addItems([d for d, _ in sorted_pairs])
        idx = self._sorted_lang_keys.index(current_key) if current_key in self._sorted_lang_keys else 0
        self.lang_combo.setCurrentIndex(idx)
        self.lang_combo.blockSignals(False)
        
        # Rebuild ui_lang_combo with names in selected language
        current_ui_key = self.ui_lang_combo.currentData() or ui_lang
        ui_display_names = UI_LANG_DISPLAY.get(ui_lang, UI_LANG_DISPLAY["English"])
        self.ui_lang_combo.blockSignals(True)
        self.ui_lang_combo.clear()
        for display, key in zip(ui_display_names, UI_LANG_KEYS):
            self.ui_lang_combo.addItem(display, key)
        ui_idx = UI_LANG_KEYS.index(current_ui_key) if current_ui_key in UI_LANG_KEYS else 0
        self.ui_lang_combo.setCurrentIndex(ui_idx)
        self.ui_lang_combo.blockSignals(False)
        
        # Rebuild help panel in selected language
        ht = HELP_TRANSLATIONS.get(ui_lang, HELP_TRANSLATIONS["English"])
        self.help_title_lbl.setText(ht["title"])
        self.help_text_lbl.setText(
            f"<p style='color:#CCC;font-size:11px;'>{ht['intro']}</p>"
            f"<p style='color:#AAA;font-size:10px;margin-top:6px;'>"
            f"<b style='color:#0078D7'>&#9889; Groq</b><br>{ht['groq_desc']}<br>"
            f"<a href='https://console.groq.com' style='color:#0078D7;'>console.groq.com</a></p>"
            f"<p style='color:#AAA;font-size:10px;margin-top:4px;'>"
            f"<b style='color:#74AA9C'>&#129302; OpenAI Whisper</b><br>{ht['openai_desc']}<br>"
            f"<a href='https://platform.openai.com/api-keys' style='color:#74AA9C;'>platform.openai.com</a></p>"
            f"<p style='color:#AAA;font-size:10px;margin-top:4px;'>"
            f"<b style='color:#CC785C'>&#129302; Anthropic (Claude)</b><br>{ht['anthropic_desc']}<br>"
            f"<a href='https://console.anthropic.com' style='color:#CC785C;'>console.anthropic.com</a></p>"
            f"<p style='color:white;font-size:10px;margin-top:8px;'>{ht['steps']}</p>"
        )

    def initTray(self):
        self.tray_icon = QSystemTrayIcon(self)
        
        # Create a simple icon programmatically
        pixmap = QPixmap(32, 32)
        pixmap.fill(Qt.GlobalColor.transparent)
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setBrush(QColor(40, 40, 40))
        painter.drawEllipse(2, 2, 28, 28)
        painter.setPen(QColor(255, 255, 255))
        font = painter.font()
        font.setPixelSize(16)
        painter.setFont(font)
        painter.drawText(pixmap.rect(), Qt.AlignmentFlag.AlignCenter, "🎤")
        painter.end()
        
        self.tray_icon.setIcon(QIcon(pixmap))
        
        tray_menu = QMenu()
        show_action = tray_menu.addAction("Show KoeScribe AI")
        show_action.triggered.connect(self.showNormal)
        tray_menu.addSeparator()
        about_action = tray_menu.addAction("About (Weslley Harakawa)")
        about_action.triggered.connect(lambda: webbrowser.open("https://github.com/weslleyharakawa"))
        tray_menu.addSeparator()
        quit_action = tray_menu.addAction("Quit")
        quit_action.triggered.connect(QApplication.instance().quit)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

    def initUI(self):
        self.setWindowTitle("KoeScribe AI")
        # Window Does Not Accept Focus is CRITICAL so we don't steal focus from the target app
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint | 
            Qt.WindowType.WindowStaysOnTopHint | 
            Qt.WindowType.WindowDoesNotAcceptFocus |
            Qt.WindowType.Tool
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setObjectName("MainWindow")
        self.setStyleSheet("QWidget#MainWindow { background: transparent; border: none; }")
        
        self.main_layout = QHBoxLayout()
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.main_layout.setSizeConstraint(QVBoxLayout.SizeConstraint.SetFixedSize)
        
        # Main Button
        self.btn = QPushButton("🎤")
        self.btn.setFont(QFont("Segoe UI Emoji", 24))
        self.btn.setFixedSize(60, 60)
        self.btn.installEventFilter(self)
        self.drag_offset = None
        self.start_global_pos = None
        self.set_button_style("default")
        
        # Settings Toggle Button (to the right of mic)
        self.btn_settings = QPushButton("⚙")
        self.btn_settings.setFixedSize(32, 32)
        self.btn_settings.setStyleSheet("border-radius: 16px; background-color: rgba(40,40,40,0.9); color: white; font-size: 14px;")
        self.btn_settings.clicked.connect(self.toggle_settings)
        
        # Left column: compact, no stretches
        from PyQt6.QtWidgets import QWidget, QSpacerItem, QSizePolicy
        self.left_col_widget = QWidget()
        self.left_col_widget.setStyleSheet("background: transparent;")
        self.left_col_widget.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.left_col_widget.setAutoFillBackground(False)
        left_vbox = QVBoxLayout(self.left_col_widget)
        left_vbox.setContentsMargins(0, 4, 0, 4)
        left_vbox.setSpacing(6)
        
        # Always-visible tiny X at top right of this column
        self.btn_close = QPushButton("✕")
        self.btn_close.setFixedSize(14, 14)
        self.btn_close.setFont(QFont("Segoe UI", 7))
        self.btn_close.setStyleSheet("""
            QPushButton {
                border-radius: 7px;
                background-color: rgba(255,255,255,0.08);
                color: rgba(255,255,255,0.3);
                border: none;
            }
            QPushButton:hover {
                background-color: rgba(220,53,69,0.85);
                color: white;
            }
        """)
        self.btn_close.clicked.connect(self.hide)
        left_vbox.addWidget(self.btn_close, alignment=Qt.AlignmentFlag.AlignRight)
        
        left_vbox.addWidget(self.btn, alignment=Qt.AlignmentFlag.AlignHCenter)
        left_vbox.addWidget(self.btn_settings, alignment=Qt.AlignmentFlag.AlignHCenter)
        left_vbox.addStretch()  # pushes coffee to the bottom
        self.btn_coffee = QLabel(
            "<div style='text-align:center;'>"
            "<span style='font-size:20px;'>\u2615</span><br>"
            "<span style='color:#888; font-size:8px; line-height:1.4;'>Buy me a<br>Coffee</span>"
            "</div>"
        )
        self.btn_coffee.setFixedSize(60, 52)
        self.btn_coffee.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.btn_coffee.setToolTip("Buy Me a Coffee")
        self.btn_coffee.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_coffee.setStyleSheet("background: transparent; border: none;")
        self.btn_coffee.mousePressEvent = lambda e: webbrowser.open("https://buymeacoffee.com/weslleyaharakawa")
        self.btn_coffee.setVisible(False)
        left_vbox.addWidget(self.btn_coffee, alignment=Qt.AlignmentFlag.AlignHCenter)
        
        # Settings Panel — title only (X is now in left column)
        self.settings_panel = QFrame()
        self.settings_panel.setStyleSheet("background-color: rgba(30,30,30,0.95); border-radius: 15px;")
        self.settings_layout = QVBoxLayout(self.settings_panel)
        
        self.title_lbl = QLabel("KoeScribe AI Settings")
        self.title_lbl.setStyleSheet("color: white; font-weight: bold; font-size: 14px; margin-bottom: 4px;")
        
        # Engine label row with help button
        engine_row = QHBoxLayout()
        self.provider_lbl = QLabel("Transcription Engine:")
        self.provider_lbl.setStyleSheet("color: #AAA; font-size: 10px;")
        self.btn_help = QPushButton("?")
        self.btn_help.setFixedSize(14, 14)
        self.btn_help.setFont(QFont("Segoe UI", 7, QFont.Weight.Bold))
        self.btn_help.setStyleSheet("""
            QPushButton {
                border-radius: 7px;
                background-color: rgba(0, 120, 215, 0.7);
                color: white;
                border: none;
            }
            QPushButton:hover { background-color: rgba(0, 120, 215, 1.0); }
        """)
        self.btn_help.clicked.connect(self.toggle_help)
        engine_row.addWidget(self.provider_lbl)
        engine_row.addWidget(self.btn_help)
        engine_row.addStretch()
        
        self.provider_combo = QComboBox()
        self.provider_combo.addItems(["Groq", "OpenAI", "Anthropic"])
        self.provider_combo.setStyleSheet("color: white; background-color: #333; padding: 5px; border-radius: 5px;")
        self.provider_combo.currentTextChanged.connect(self.on_provider_changed)
        
        self.key_lbl = QLabel("API Key:")
        self.key_lbl.setStyleSheet("color: #AAA; font-size: 10px;")
        
        self.key_input = QLineEdit()
        self.key_input.setPlaceholderText("Paste your API key here")
        self.key_input.setStyleSheet("color: white; background-color: #333; padding: 5px; border-radius: 5px;")
        
        self.ui_lang_lbl = QLabel("Interface Language:")
        self.ui_lang_lbl.setStyleSheet("color: #AAA; font-size: 10px;")
        
        self.ui_lang_combo = QComboBox()
        for _native, _key in [
            ("English",    "English"),
            ("Português",  "Portuguese"),
            ("Español",    "Spanish"),
            ("日本語",     "Japanese"),
            ("中文",       "Chinese"),
            ("Nederlands", "Dutch"),
        ]:
            self.ui_lang_combo.addItem(_native, _key)
        self.ui_lang_combo.setStyleSheet("color: white; background-color: #333; padding: 5px; border-radius: 5px;")
        self.ui_lang_combo.currentIndexChanged.connect(self.on_ui_lang_changed)
        
        self.lang_lbl = QLabel("Transcription Language:")
        self.lang_lbl.setStyleSheet("color: #AAA; font-size: 10px;")
        
        self.lang_combo = QComboBox()
        self.lang_combo.addItems(AUDIO_LANG_KEYS)  # will be overwritten by apply_translation
        self.lang_combo.setStyleSheet("color: white; background-color: #333; padding: 5px; border-radius: 5px;")
        
        self.save_btn = QPushButton("Save")
        self.save_btn.setStyleSheet("background-color: #0078D7; color: white; padding: 5px; border-radius: 5px; font-weight: bold; margin-top: 5px;")
        self.save_btn.clicked.connect(self.save_config)
        
        self.about_lbl = QLabel('<a href="https://github.com/weslleyharakawa" style="color: #0078D7; text-decoration: none;">KoeScribe AI • Developed by Weslley Harakawa</a>')
        self.about_lbl.setOpenExternalLinks(False)
        self.about_lbl.linkActivated.connect(lambda url: webbrowser.open(url))
        self.about_lbl.setStyleSheet("font-size: 10px; margin-top: 5px;")
        
        self.settings_layout.addWidget(self.title_lbl)
        self.settings_layout.addWidget(self.ui_lang_lbl)
        self.settings_layout.addWidget(self.ui_lang_combo)
        self.settings_layout.addLayout(engine_row)
        self.settings_layout.addWidget(self.provider_combo)
        self.settings_layout.addWidget(self.key_lbl)
        self.settings_layout.addWidget(self.key_input)
        self.settings_layout.addWidget(self.lang_lbl)
        self.settings_layout.addWidget(self.lang_combo)
        self.settings_layout.addWidget(self.save_btn)
        self.settings_layout.addWidget(self.about_lbl)
        
        self.settings_panel.setVisible(False)
        
        # Help Panel (expands to the right of settings)
        self.help_panel = QFrame()
        self.help_panel.setStyleSheet("background-color: rgba(20,20,30,0.97); border-radius: 15px;")
        self.help_panel.setFixedWidth(260)
        help_layout = QVBoxLayout(self.help_panel)
        
        help_title = QLabel("")
        help_title.setStyleSheet("color: white; font-weight: bold; font-size: 13px; margin-bottom: 4px;")
        
        self.help_title_lbl = help_title
        self.help_text_lbl = QLabel()
        self.help_text_lbl.setWordWrap(True)
        self.help_text_lbl.setOpenExternalLinks(False)
        self.help_text_lbl.linkActivated.connect(lambda url: webbrowser.open(url))
        
        help_layout.addWidget(self.help_title_lbl)
        help_layout.addWidget(self.help_text_lbl)
        help_layout.addStretch()
        self.help_panel.setVisible(False)
        
        self.main_layout.addWidget(self.left_col_widget)
        self.main_layout.addWidget(self.settings_panel)
        self.main_layout.addWidget(self.help_panel)
        self.setLayout(self.main_layout)

    def toggle_help(self):
        self.help_panel.setVisible(not self.help_panel.isVisible())

    def toggle_settings(self):
        visible = not self.settings_panel.isVisible()
        self.settings_panel.setVisible(visible)
        self.btn_coffee.setVisible(visible)
        if visible:
            provider = self.config.get("provider", "Groq")
            self.provider_combo.setCurrentText(provider)
            self.key_input.setText(self.config["keys"].get(provider, ""))
            self.ui_lang_combo.blockSignals(True)
            saved_ui_lang = self.config.get("ui_language", "English")
            for i in range(self.ui_lang_combo.count()):
                if self.ui_lang_combo.itemData(i) == saved_ui_lang:
                    self.ui_lang_combo.setCurrentIndex(i)
                    break
            self.ui_lang_combo.blockSignals(False)
            # Set lang_combo to translated name of saved key
            ui_lang = self.config.get("ui_language", "English")
            lang_key = self.config.get("language", "Portuguese (Brazil)")
            display_names = AUDIO_LANG_DISPLAY.get(ui_lang, AUDIO_LANG_DISPLAY["English"])
            idx = AUDIO_LANG_KEYS.index(lang_key) if lang_key in AUDIO_LANG_KEYS else 0
            self.lang_combo.blockSignals(True)
            self.lang_combo.clear()
            self.lang_combo.addItems(display_names)
            self.lang_combo.setCurrentIndex(idx)
            self.lang_combo.blockSignals(False)

    def on_provider_changed(self, provider):
        self.key_input.setText(self.config["keys"].get(provider, ""))

    def on_ui_lang_changed(self, index):
        # Apply instantly without saving
        lang = self.ui_lang_combo.itemData(index)
        if not lang:
            return
        old_lang = self.config.get("ui_language", "English")
        self.config["ui_language"] = lang
        self.apply_translation()
        self.config["ui_language"] = old_lang  # Don't persist yet — only on Save

    def set_button_style(self, state):
        base_style = """
            QPushButton {
                border-radius: 30px;
                color: white;
                font-weight: bold;
                border: 2px solid rgba(255, 255, 255, 0.2);
            }
        """
        if state == "default":
            self.btn.setText("🎤")
            self.btn.setStyleSheet(base_style + """
                QPushButton {
                    background-color: rgba(40, 40, 40, 0.9);
                }
                QPushButton:hover {
                    background-color: rgba(60, 60, 60, 0.9);
                }
            """)
        elif state == "recording":
            self.btn.setText("🛑")
            self.btn.setStyleSheet(base_style + """
                QPushButton {
                    background-color: rgba(220, 53, 69, 0.9);
                    border: 2px solid rgba(255, 255, 255, 0.5);
                }
            """)
        elif state == "processing":
            self.btn.setText("⏳")
            self.btn.setStyleSheet(base_style + """
                QPushButton {
                    background-color: rgba(23, 162, 184, 0.9);
                }
            """)

    def toggle_recording(self):
        if self.is_processing:
            return
        if not self.is_recording:
            self.start_recording()
        else:
            self.stop_recording()

    def start_recording(self):
        # Prevent starting if API key is empty
        provider = self.config.get("provider", "Groq")
        if not self.config["keys"].get(provider, ""):
            self.toggle_settings()
            return
            
        self.is_recording = True
        self.is_processing = False
        self.audio_data = []
        self.last_typed = ""
        self.set_button_style("recording")
        
        def callback(indata, frames, time, status):
            if status:
                pass
            self.audio_data.extend(indata.copy())

        self.stream = sd.InputStream(samplerate=self.samplerate, channels=1, callback=callback)
        self.stream.start()
        
        # Start processing thread
        threading.Thread(target=self.recording_thread).start()

    def stop_recording(self):
        self.is_recording = False
        self.is_processing = True
        self.set_button_style("processing")
        if self.stream:
            self.stream.stop()
            self.stream.close()

    def _transcribe_audio_buffer(self):
        if len(self.audio_data) < self.samplerate * 0.5:
            return ""
        try:
            audio_np = np.array(self.audio_data)
            audio_int16 = (audio_np * 32767).astype(np.int16)
            
            temp_dir = tempfile.gettempdir()
            temp_file = os.path.join(temp_dir, "temp_rt_audio.wav")
            
            with wave.open(temp_file, 'wb') as wf:
                wf.setnchannels(1)
                wf.setsampwidth(2)
                wf.setframerate(self.samplerate)
                wf.writeframes(audio_int16.tobytes())
                
            provider = self.config.get("provider", "Groq")
            key = self.config["keys"].get(provider, "")
            
            lang_sel = self.config.get("language", "Portuguese (Brazil)")
            lang_code = "pt"
            prompt_text = "Transcreva em português do Brasil. O texto é ditado."
            
            if lang_sel == "Portuguese (Brazil)":
                lang_code = "pt"
                prompt_text = "Transcreva em português do Brasil. O texto é ditado."
            elif lang_sel == "Portuguese (Portugal)":
                lang_code = "pt"
                prompt_text = "Transcreva em português de Portugal. O texto é ditado."
            elif lang_sel == "English (USA)":
                lang_code = "en"
                prompt_text = "Transcribe in American English. The text is dictated."
            elif lang_sel == "English (British)":
                lang_code = "en"
                prompt_text = "Transcribe in British English. The text is dictated."
            elif lang_sel == "Spanish (Latin America)":
                lang_code = "es"
                prompt_text = "Transcribe en español de América Latina. El texto es dictado."
            elif lang_sel == "Spanish (Spain)":
                lang_code = "es"
                prompt_text = "Transcribe en español de España. El texto es dictado."
            elif lang_sel == "Japanese":
                lang_code = "ja"
                prompt_text = "日本語で書き起こしてください。音声入力です。"
            elif lang_sel == "Chinese":
                lang_code = "zh"
                prompt_text = "请用简体中文进行转录。这是语音输入。"
            
            text = ""
            if provider == "Groq":
                from groq import Groq
                client = Groq(api_key=key)
                with open(temp_file, "rb") as file:
                    transcription = client.audio.transcriptions.create(
                        file=(temp_file, file.read()),
                        model="whisper-large-v3-turbo",
                        prompt=prompt_text,
                        language=lang_code,
                        temperature=0.0
                    )
                text = transcription.text.strip()
                
            elif provider == "OpenAI":
                from openai import OpenAI
                client = OpenAI(api_key=key)
                with open(temp_file, "rb") as file:
                    transcription = client.audio.transcriptions.create(
                        file=file,
                        model="whisper-1",
                        prompt=prompt_text,
                        language=lang_code,
                        temperature=0.0
                    )
                text = transcription.text.strip()
                
            elif provider == "Anthropic":
                # Anthropic doesn't have an audio transcription model yet.
                text = "[A Anthropic ainda não suporta transcrição de áudio.]"

            os.remove(temp_file)
            return text
        except Exception as e:
            print(f"API Error: {e}")
            return ""

    def recording_thread(self):
        import time
        while self.is_recording:
            # Wait for 1.5 seconds in small increments
            for _ in range(15):
                if not self.is_recording:
                    break
                time.sleep(0.1)
                
            if not self.is_recording:
                break
                
            text = self._transcribe_audio_buffer()
            if text:
                self.signals.realtime_update.emit(text)

        # Finished recording loop, now do final transcription
        text = self._transcribe_audio_buffer()
        if text:
            self.signals.realtime_update.emit(text)
        
        self.signals.finished.emit()

    def on_realtime_update(self, new_text):
        old_text = getattr(self, 'last_typed', "")
        
        # Find common prefix length
        common_len = 0
        for i in range(min(len(old_text), len(new_text))):
            if old_text[i] == new_text[i]:
                common_len += 1
            else:
                break
                
        backspaces = len(old_text) - common_len
        for _ in range(backspaces):
            keyboard.send('backspace')
            
        new_chars = new_text[common_len:]
        if new_chars:
            keyboard.write(new_chars)
            
        self.last_typed = new_text

    def on_finished(self):
        self.is_processing = False
        self.set_button_style("default")
        # Add a trailing space to end the dictation block
        keyboard.write(" ")

    def on_error(self, err):
        self.is_processing = False
        self.set_button_style("default")
        print(f"Error: {err}")

    def eventFilter(self, obj, event):
        if obj == self.btn:
            if event.type() == event.Type.MouseButtonPress:
                if event.button() == Qt.MouseButton.LeftButton:
                    self.drag_offset = event.pos()
                    self.start_global_pos = event.globalPosition().toPoint()
                    return True # Consume event
            elif event.type() == event.Type.MouseMove:
                if event.buttons() == Qt.MouseButton.LeftButton and self.drag_offset is not None:
                    # Safely move without jitter
                    # Offset calculation accounts for widget margins
                    self.move(event.globalPosition().toPoint() - self.drag_offset - self.btn.pos())
                    return True
            elif event.type() == event.Type.MouseButtonRelease:
                if event.button() == Qt.MouseButton.LeftButton:
                    self.drag_offset = None
                    # If it didn't move much, it's a click
                    if self.start_global_pos and (event.globalPosition().toPoint() - self.start_global_pos).manhattanLength() < 5:
                        self.toggle_recording()
                    return True
        return super().eventFilter(obj, event)

    # Allow dragging from empty areas of the window as well
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.window_drag_offset = event.pos()

    def mouseMoveEvent(self, event):
        if hasattr(self, 'window_drag_offset') and event.buttons() == Qt.MouseButton.LeftButton:
            self.move(event.globalPosition().toPoint() - self.window_drag_offset)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False) # Keep running when main window is hidden
    ex = RecorderApp()
    ex.show()
    sys.exit(app.exec())
