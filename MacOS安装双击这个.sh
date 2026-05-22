#!/bin/bash

echo "========================================"
echo "SnowAI Assistant - macOS Installer"
echo "========================================"
echo ""

# Get script directory
cd "$(dirname "$0")"
APP_DIR="$(pwd)"

echo "Install dir: $APP_DIR"
echo ""

# ========== Check Homebrew ==========
echo "[1/5] Checking Homebrew..."
if ! command -v brew &> /dev/null; then
    echo "  Homebrew not found, installing..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
else
    echo "  Homebrew already installed"
fi

# ========== Install OCR Tools ==========
echo ""
echo "[2/5] Installing OCR tools..."
brew install poppler tesseract tesseract-lang

# ========== Check Python ==========
echo ""
echo "[3/5] Checking Python..."
if ! command -v python3 &> /dev/null; then
    echo "  Python3 not found, please install Python 3.11+"
    echo "  Download from: https://www.python.org/downloads/"
    exit 1
fi
echo "  Python3: $(python3 --version)"

# ========== Install Python Dependencies ==========
echo ""
echo "[4/5] Installing Python dependencies..."
pip3 install --upgrade pip
pip3 install PySide6 openai requests markdown python-dotenv pandas
pip3 install python-docx PyPDF2 pdf2image pytesseract pycryptodome
pip3 install chromadb sentence-transformers transformers torch
pip3 install openpyxl

# ========== Download AI Model ==========
echo ""
echo "[5/5] Downloading AI model..."
python3 -c "from sentence_transformers import SentenceTransformer; model = SentenceTransformer('BAAI/bge-small-zh'); model.save('_model/bge-small-zh')"

if [ -d "$APP_DIR/_model/bge-small-zh" ]; then
    echo "  AI model downloaded"
else
    echo "  Model download may have failed"
fi

# ========== Create Launcher ==========
echo ""
echo "Creating launcher..."

cat > "$APP_DIR/start.command" << 'EOF'
#!/bin/bash
cd "$(dirname "$0")"
echo "Starting SnowAI..."
python3 main.py
echo ""
echo "Press any key to exit..."
read -n1
EOF

chmod +x "$APP_DIR/start.command"

# ========== Create Desktop Shortcut ==========
ln -sf "$APP_DIR/start.command" ~/Desktop/SnowAI
echo "Desktop shortcut created"

echo ""
echo "========================================"
echo "      Installation Complete!"
echo "========================================"
echo ""
echo "Usage:"
echo "   Double-click SnowAI on desktop"
echo ""
echo "If you have problems, please send error message to Snow~"
echo ""
