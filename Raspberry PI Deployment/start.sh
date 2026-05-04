
Gemini

Generate your next big idea with Gemini in Gmail, Docs, and more
Power up your productivity with AI features directly in the apps you use every day

Create drafts in Docs

Plan projects quickly in Sheets

Generate original images in Slides

Start enhanced meetings in Meet
Plus, get access to Gemini Pro with our most capable AI models and more storage
Already signed up? Refresh this page
#!/bin/bash
# start.sh — Start WildTrack AI on Raspberry Pi 5

PROJECT_DIR="/home/abs/Desktop/wildtrack"
VENV_DIR="$PROJECT_DIR/venv"

echo "🌲 Starting WildTrack AI..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
PI_IP=$(hostname -I | awk '{print $1}')
echo "📡 Pi IP Address : $PI_IP"
echo "🌐 Dashboard     : http://$PI_IP:8000"
echo "📷 Stream        : http://$PI_IP:8000/stream"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

if [ ! -d "$PROJECT_DIR" ]; then echo "❌ Project folder not found: $PROJECT_DIR"; exit 1; fi
if [ ! -f "$PROJECT_DIR/best.pt" ]; then echo "❌ Missing best.pt in $PROJECT_DIR"; exit 1; fi

cd "$PROJECT_DIR"

if [ ! -d "$VENV_DIR" ]; then
  echo "⚙️  Creating venv (--system-site-packages for picamera2/libcamera/opencv)..."
  python3 -m venv --system-site-packages "$VENV_DIR"
  source "$VENV_DIR/bin/activate"
  pip install --upgrade pip --quiet

  echo "📦 Installing packages..."
  # We do NOT install numpy or opencv here — we use the system versions
  # (numpy 2.4.4 + opencv 4.13.0.92) which are already compatible with each other.
  pip install \
    "fastapi==0.115.6" \
    "uvicorn==0.29.0" \
    "python-multipart==0.0.9" \
    "ultralytics==8.4.37" \
    "click>=8.1.7" \
    "Pillow" \
    --quiet
  echo "✓ Done"
else
  source "$VENV_DIR/bin/activate"
fi

export PYTHONPATH="$PROJECT_DIR"
mkdir -p "$PROJECT_DIR/frames"

echo "🔍 Checking imports..."
"$VENV_DIR/bin/python" - << 'PYCHECK'
import sys, importlib
ok = True
for mod, label in [
    ("numpy",       "numpy"),
    ("cv2",         "cv2"),
    ("fastapi",     "fastapi"),
    ("uvicorn",     "uvicorn"),
    ("ultralytics", "ultralytics"),
    ("picamera2",   "picamera2"),
    ("libcamera",   "libcamera"),
]:
    try:
        m = importlib.import_module(mod)
        print(f"  ✓ {label} {getattr(m,'__version__','')}")
    except Exception as e:
        print(f"  ❌ {label}: {e}"); ok = False
if not ok: sys.exit(1)
print("  ✅ All OK")
PYCHECK

if [ $? -ne 0 ]; then
  echo "❌ Fix errors above. If stuck: rm -rf $VENV_DIR && ./start.sh"
  exit 1
fi

echo ""
echo "🚀 Starting server..."
"$VENV_DIR/bin/python" -m uvicorn api.main:app \
  --host 0.0.0.0 --port 8000 --workers 1 --log-level info
