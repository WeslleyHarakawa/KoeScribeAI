#!/bin/bash
# KoeScribe AI - macOS Build Script
# Run this on a Mac with Python 3.11+ installed
# Requirements: pip install pyinstaller PyQt6 groq sounddevice numpy keyboard openai anthropic

set -e

echo "=== KoeScribe AI macOS Build ==="
echo "Installing dependencies..."
pip3 install PyQt6 groq sounddevice numpy keyboard openai anthropic pyinstaller

echo "Building .app bundle..."
pyinstaller \
  --onefile \
  --windowed \
  --name "KoeScribe AI" \
  --add-data "bmc_logo.png:." \
  app.py

echo ""
echo "Build complete! App is in: dist/KoeScribe AI.app"
echo "You can also find the .app in the dist/ folder."
echo ""
echo "NOTE: On macOS you may need to grant permissions:"
echo "  - Microphone access (System Preferences > Privacy > Microphone)"
echo "  - Accessibility access for keyboard typing (System Preferences > Privacy > Accessibility)"
