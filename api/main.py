"""
api/main.py
FastAPI for Raspberry Pi deployment.
Serves live camera feed, detection results, history, and the permanent log file.
"""

from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, StreamingResponse, HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import cv2
import numpy as np
import io
import time

from model.detect import state, start_detection, LEGALITY, DETECTION_LOG_TXT, DETECTION_LOG_CSV
from ultralytics import YOLO

app = FastAPI(title="WildTrack AI — Pi Edition", version="3.1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

if Path("ui").exists():
    app.mount("/ui", StaticFiles(directory="ui"), name="ui")

@app.on_event("startup")
async def startup():
    print("Starting detection loop...")
    start_detection()
    print("✓ WildTrack AI running on Raspberry Pi")

# ── Health ─────────────────────────────────────────────────────────────────────
@app.get("/health")
def health():
    with state.lock:
        return {
            "status":           "ok",
            "running":          state.running,
            "total_frames":     state.total_frames,
            "total_detections": state.total_detections,
            "fps":              state.fps,
            "motion_state":     state.motion_state,
            "motion_pct":       state.motion_pct,
        }

# ── Latest result ──────────────────────────────────────────────────────────────
@app.get("/latest")
def get_latest():
    with state.lock:
        if state.latest_result is None:
            return {"status": "waiting", "message": "No frames captured yet"}
        return state.latest_result

# ── History ────────────────────────────────────────────────────────────────────
@app.get("/history")
def get_history(limit: int = 20):
    with state.lock:
        return {
            "results": state.history[-limit:],
            "total":   len(state.history)
        }

# ── Permanent detection log (download) ─────────────────────────────────────────
@app.get("/log")
def download_log():
    """Download the permanent detection log file."""
    if not DETECTION_LOG.exists():
        return JSONResponse(status_code=404, content={"error": "No log file found"})
    return FileResponse(
        path=DETECTION_LOG,
        media_type="text/plain",
        filename="wildtrack_detections.txt"
    )

@app.get("/log/view")
def view_log():
    """View the detection log as plain text in the browser."""
    if not DETECTION_LOG.exists():
        return JSONResponse(status_code=404, content={"error": "No log file found"})
    content = DETECTION_LOG.read_text(encoding="utf-8")
    return HTMLResponse(f"<pre style='font-family:monospace;padding:2rem;'>{content}</pre>")

# ── Frame endpoints ────────────────────────────────────────────────────────────
@app.get("/frame/raw")
def get_raw_frame():
    with state.lock:
        jpg = state.latest_frame_jpg
    if jpg is None:
        return JSONResponse(status_code=503, content={"error": "No frame available yet"})
    return StreamingResponse(io.BytesIO(jpg), media_type="image/jpeg")

@app.get("/frame/annotated")
def get_annotated_frame():
    with state.lock:
        jpg = state.latest_annotated_jpg
    if jpg is None:
        return JSONResponse(status_code=503, content={"error": "No frame available yet"})
    return StreamingResponse(io.BytesIO(jpg), media_type="image/jpeg")

@app.get("/stream")
def mjpeg_stream():
    """MJPEG live stream of annotated frames."""
    def generate():
        while True:
            with state.lock:
                jpg = state.latest_annotated_jpg
            if jpg:
                yield (
                    b"--frame\r\n"
                    b"Content-Type: image/jpeg\r\n\r\n" + jpg + b"\r\n"
                )
            time.sleep(0.1)

    return StreamingResponse(
        generate(),
        media_type="multipart/x-mixed-replace;boundary=frame"
    )

# ── Manual detect (upload image) ───────────────────────────────────────────────
_manual_model = None

@app.post("/detect")
async def detect_upload(file: UploadFile = File(...)):
    global _manual_model
    if _manual_model is None:
        _manual_model = YOLO("best.pt")

    image_bytes = await file.read()
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    if img is None:
        return JSONResponse(status_code=400, content={"error": "Invalid image"})

    img_resized = cv2.resize(img, (640, 640))
    results = _manual_model.predict(img_resized, conf=0.35, verbose=False)
    result = results[0]

    detections = []
    for box in result.boxes:
        class_id   = int(box.cls[0])
        confidence = float(box.conf[0])
        species    = _manual_model.names.get(class_id, "unknown")
        detections.append({
            "species":    species,
            "confidence": round(confidence, 4),
            "bbox":       [round(v, 1) for v in box.xyxy[0].tolist()],
            "legal":      LEGALITY.get(species, "illegal")
        })

    return {
        "image":          file.filename,
        "animal_present": len(detections) > 0,
        "detections":     detections,
        "empty_frame":    len(detections) == 0
    }

# ── Root → redirect to UI ──────────────────────────────────────────────────────
@app.get("/")
def root():
    return HTMLResponse("""
    <html><head><meta http-equiv="refresh" content="0;url=/ui/index.html"></head>
    <body>Redirecting to WildTrack AI dashboard...</body></html>
    """)
