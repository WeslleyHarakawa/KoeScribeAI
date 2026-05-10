c = open('app.py', encoding='utf-8').read()
old = (
    "Convert displayed lang name back to internal key\n"
    "        display_idx = self.lang_combo.currentIndex()\n"
    "        lang_key = AUDIO_LANG_KEYS[display_idx] if 0 <= display_idx < len(AUDIO_LANG_KEYS) else \"Portuguese (Brazil)\""
)
new = (
    "Convert displayed (sorted) lang index back to internal key\n"
    "        display_idx = self.lang_combo.currentIndex()\n"
    "        sorted_keys = getattr(self, '_sorted_lang_keys', AUDIO_LANG_KEYS)\n"
    "        lang_key = sorted_keys[display_idx] if 0 <= display_idx < len(sorted_keys) else \"Portuguese (Brazil)\""
)
print("found:", old in c)
c2 = c.replace(old, new, 1)
open('app.py', 'w', encoding='utf-8').write(c2)
print("done")
