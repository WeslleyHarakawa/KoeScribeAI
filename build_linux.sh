#!/bin/bash
# KoeScribe AI - Linux (Ubuntu) Build Script
# Run this on Ubuntu with Python 3.11+ installed

set -e

echo "=== KoeScribe AI Linux Build ==="
echo "Installing system dependencies..."
sudo apt-get update -qq
sudo apt-get install -y python3-pip python3-venv portaudio19-dev python3-pyaudio libxcb-xinerama0

echo "Creating virtual environment..."
python3 -m venv venv_linux
source venv_linux/bin/activate

echo "Installing Python dependencies..."
pip install PyQt6 groq sounddevice numpy keyboard openai anthropic pyinstaller

echo "Building Linux binary..."
pyinstaller \
  --onefile \
  --windowed \
  --name "KoeScribeAI" \
  --add-data "bmc_logo.png:." \
  app.py

echo ""
echo "Build complete! Binary is in: dist/KoeScribeAI"
echo ""
echo "NOTE: On Linux the 'keyboard' library requires root to simulate keystrokes."
echo "Run the app with: sudo ./KoeScribeAI"
echo "Or add your user to the 'input' group: sudo usermod -a -G input \$USER"
