
Gemini

Generate your next big idea with Gemini in Gmail, Docs, and more
Power up your productivity with AI features directly in the apps you use every day

Create drafts in Docs

Plan projects quickly in Sheets

Generate original images in Slides

Start enhanced meetings in Meet
Plus, get access to Gemini Pro with our most capable AI models and more storage
Already signed up? Refresh this page
# WildTrack AI — Raspberry Pi 5 Edition

Wildlife detection system using YOLOv8n + Pi Camera V3.
Detects animals automatically, flags hunting legality, streams live to any browser.

## Setup on Raspberry Pi

### 1. Copy the wildtrack folder to your Desktop
```bash
scp -r wildtrack/ abs@PI_IP_ADDRESS:/home/abs/Desktop/
```

### 2. Put your model in place
```
wildtrack/
└── best.pt   ← copy from Google Drive
```

### 3. Start
```bash
cd /home/abs/Desktop/wildtrack
chmod +x start.sh
./start.sh
```
The script will automatically create a virtual environment and install
all dependencies on the first run.

### 4. Open the dashboard
Open any browser on the same WiFi network:
```
http://PI_IP_ADDRESS:8000
```

---

## Folder structure
```
wildtrack/
├── api/
│   ├── __init__.py
│   └── main.py          ← FastAPI server
├── model/
│   ├── __init__.py
│   └── detect.py        ← Detection loop
├── ui/
│   └── index.html       ← Live dashboard
├── frames/              ← Saved detection frames (auto-created)
├── best.pt              ← YOLOv8n model  ← YOU MUST ADD THIS
├── requirements.txt
└── start.sh             ← One-command startup
```

---

## API Endpoints
| Method | Path               | Description                        |
|--------|--------------------|------------------------------------|
| GET    | `/`                | Dashboard redirect                 |
| GET    | `/health`          | System status + FPS                |
| GET    | `/latest`          | Most recent detection result       |
| GET    | `/history`         | Last 20 detections                 |
| GET    | `/frame/raw`       | Latest raw camera frame (JPEG)     |
| GET    | `/frame/annotated` | Latest annotated frame (JPEG)      |
| GET    | `/stream`          | MJPEG live stream                  |
| POST   | `/detect`          | Manual image upload detection      |

---

## Species & Legality
| Species  | Legal Status |
|----------|-------------|
| Deer     | ✅ Legal    |
| Boar     | ✅ Legal    |
| Rabbit   | ✅ Legal    |
| Pheasant | ✅ Legal    |
| Jackal   | ⛔ Illegal  |

---

## What was fixed

### 🎨 Colour accuracy (blue tint)
The original code used `create_still_configuration` which restarts the camera
ISP on every capture — auto white balance never had time to settle, causing a
blue/cool colour cast. Fixed by:
- Switching to `create_video_configuration` (ISP stays warm continuously)
- Waiting 3 seconds after startup, reading the settled AWB gains from
  `capture_metadata()`, then locking them with `AwbEnable: False`

### 🚫 False positives
Confidence threshold was 0.35 which is too permissive for field use.
Fixed by:
- Raising confidence threshold to 0.55
- Adding explicit NMS `iou=0.45` to suppress duplicate boxes
- Adding a **temporal filter**: a species must appear in at least 2 of the
  last 3 consecutive frames before it is reported as a real detection.
  Single-frame ghost detections (shadows, motion blur) are silently dropped.
  Filtered boxes are still drawn in grey on the annotated frame so you can
  see what is being suppressed.

### ⚡ Performance / 2.5 s interval
`create_still_configuration` at 1920×1080 took 1–2 seconds per capture.
Fixed by:
- `create_video_configuration` at 1280×720 keeps the ISP pipeline hot
- A dedicated camera thread grabs frames continuously into a shared buffer
- The inference loop copies from that buffer — no waiting on the camera
- Capture interval set to 2.5 s as requested
- The `/stream` MJPEG endpoint only pushes a new frame when the annotated
  image actually changes — no busy-spinning
