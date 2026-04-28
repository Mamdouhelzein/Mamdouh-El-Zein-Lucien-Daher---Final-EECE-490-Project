"""
model/detect.py
Motion-triggered live detection window.

Behavior:
- Idle until motion is detected.
- Once motion is detected, opens a 5-second LIVE window.
- During the 5-second window, runs YOLO continuously and updates live feed.
- Counting/logging rule:
    * A non-empty frame after an empty frame = new detection event.
    * Continuous same animal across non-empty frames counts once.
    * If multiple animals appear in that new event frame, all are logged.
"""

import time
import threading
import cv2
import numpy as np
from datetime import datetime
from pathlib import Path
from picamera2 import Picamera2
from libcamera import Transform
from ultralytics import YOLO

# ── Config ─────────────────────────────────────────────────────────────────────
MODEL_PATH         = "best.pt"
CONF_THRESHOLD     = 0.55
MIN_BOX_AREA       = 2500
IMG_SIZE           = 640

# Motion trigger only starts the live window
MOTION_THRESHOLD   = 5.0
FRAME_DIFF_BLUR    = 21
LIVE_WINDOW_MS     = 5000

MAX_HISTORY        = 50
SAVE_FRAMES        = True
FRAMES_DIR         = Path("frames")
DETECTION_LOG      = Path("detections.txt")

LEGALITY = {
    "deer":     "legal",
    "boar":     "legal",
    "rabbit":   "legal",
    "pheasant": "legal",
    "jackal":   "illegal",
}

FRAMES_DIR.mkdir(exist_ok=True)

# ── Permanent detection log ────────────────────────────────────────────────────
_log_lock = threading.Lock()

def log_detection(timestamp: str, detection: dict):
    """Append a detection to the permanent log file."""
    line = (
        f"{timestamp}\t"
        f"{detection['species']}\t"
        f"{detection['confidence']:.4f}\t"
        f"{detection['legal']}\n"
    )
    with _log_lock:
        with open(DETECTION_LOG, "a", encoding="utf-8") as f:
            f.write(line)

if not DETECTION_LOG.exists() or DETECTION_LOG.stat().st_size == 0:
    with open(DETECTION_LOG, "w", encoding="utf-8") as f:
        f.write("# WildTrack Detection Log\n")
        f.write("# Format: timestamp\\tspecies\\tconfidence\\tlegal_status\n")

# ── Shared state ───────────────────────────────────────────────────────────────
class DetectionState:
    def __init__(self):
        self.lock = threading.Lock()
        self.latest_frame_jpg     = None
        self.latest_annotated_jpg = None
        self.latest_result        = None
        self.history              = []
        self.running              = False
        self.fps                  = 0.0
        self.total_frames         = 0
        self.total_detections     = 0   # event-style count
        self.motion_state         = "idle"
        self.motion_pct           = 0.0

state = DetectionState()

# ── Helpers ────────────────────────────────────────────────────────────────────
def to_jpeg(img_bgr):
    _, buf = cv2.imencode(".jpg", img_bgr, [cv2.IMWRITE_JPEG_QUALITY, 85])
    return buf.tobytes()

def compute_motion(prev_gray, curr_gray):
    diff = cv2.absdiff(prev_gray, curr_gray)
    _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
    return (np.sum(thresh > 0) / thresh.size) * 100.0

def run_inference(model, frame_bgr):
    results = model.predict(
        source=frame_bgr,
        conf=CONF_THRESHOLD,
        verbose=False,
        imgsz=IMG_SIZE,
    )
    result = results[0]

    detections = []
    annotated = frame_bgr.copy()

    for box in result.boxes:
        x1, y1, x2, y2 = box.xyxy[0].tolist()
        area = (x2 - x1) * (y2 - y1)
        if area < MIN_BOX_AREA:
            continue

        class_id   = int(box.cls[0])
        confidence = float(box.conf[0])
        species    = model.names.get(class_id, "unknown")
        legal      = LEGALITY.get(species, "illegal")

        detections.append({
            "species":    species,
            "confidence": round(confidence, 4),
            "bbox":       [round(v, 1) for v in [x1, y1, x2, y2]],
            "legal":      legal
        })

        color = (0, 255, 127) if legal == "legal" else (82, 82, 224)
        cv2.rectangle(annotated, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)
        label = f"{species} {confidence:.0%}"
        cv2.putText(
            annotated,
            label,
            (int(x1), max(int(y1) - 8, 15)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            color,
            2,
        )

    return detections, annotated

def dedupe_event_detections(detections):
    """
    Keep one detection per species for event counting/logging.
    If multiple boxes of same species appear, keep the highest confidence one.
    """
    best_by_species = {}
    for det in detections:
        species = det["species"]
        if species not in best_by_species or det["confidence"] > best_by_species[species]["confidence"]:
            best_by_species[species] = det
    return list(best_by_species.values())

# ── Main detection loop ────────────────────────────────────────────────────────
def detection_loop():
    print("Loading model...")
    model = YOLO(MODEL_PATH)
    print(f"✓ Model loaded: {MODEL_PATH}")

    print("Starting camera at 640x640...")
    camera = Picamera2()
    config = camera.create_still_configuration(
        main={"size": (640, 640), "format": "RGB888"},
        transform=Transform(vflip=1)
    )
    camera.configure(config)
    camera.start()
    time.sleep(2.0)
    camera.set_controls({"AwbEnable": True})
    print("  AWB set to auto")
    print("✓ Camera ready — MOTION -> 5s LIVE WINDOW mode")
    print(f"   Motion threshold: {MOTION_THRESHOLD}%")
    print(f"   Live window: {LIVE_WINDOW_MS}ms")
    print(f"   Log file: {DETECTION_LOG.absolute()}")

    state.running = True

    prev_gray = None
    live_until_ms = 0
    previous_frame_had_animal = False

    while state.running:
        loop_start = time.time()

        try:
            # Capture current frame
            frame_rgb = camera.capture_array("main")
            frame_bgr = frame_rgb

            gray = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2GRAY)
            gray_blur = cv2.GaussianBlur(gray, (FRAME_DIFF_BLUR, FRAME_DIFF_BLUR), 0)

            now_ms = time.time() * 1000
            motion_pct = 0.0

            if prev_gray is not None:
                motion_pct = compute_motion(prev_gray, gray_blur)

            # Trigger 5-second live window when motion starts
            if now_ms >= live_until_ms and motion_pct > MOTION_THRESHOLD:
                live_until_ms = now_ms + LIVE_WINDOW_MS
                previous_frame_had_animal = False
                print(f"⚡ Motion detected: {motion_pct:.1f}% — LIVE for 5 seconds")

            in_live_window = now_ms < live_until_ms

            with state.lock:
                state.motion_pct = round(motion_pct, 2)
                state.motion_state = "detected" if in_live_window else "idle"

            if in_live_window:
                t0 = time.time()
                detections, annotated = run_inference(model, frame_bgr)
                latency_ms = round((time.time() - t0) * 1000, 1)
                animal_present = len(detections) > 0

                timestamp = datetime.now().isoformat()
                timestamp_readable = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # Event rule:
                # only count/log when current frame has animals AND previous frame was empty
                new_event = animal_present and not previous_frame_had_animal
                event_detections = dedupe_event_detections(detections) if new_event else []

                if new_event:
                    for det in event_detections:
                        log_detection(timestamp_readable, det)
                        print(f"   📝 Logged new event: {det['species']} ({det['confidence']:.0%}) [{det['legal']}]")

                result_dict = {
                    "timestamp":      timestamp,
                    "animal_present": animal_present,
                    "detections":     detections,
                    "latency_ms":     latency_ms,
                    "frame_count":    state.total_frames + 1,
                    "motion_pct":     round(motion_pct, 2),
                }

                if animal_present and SAVE_FRAMES:
                    fname = FRAMES_DIR / f"{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}.jpg"
                    cv2.imwrite(str(fname), annotated)

                with state.lock:
                    state.latest_frame_jpg     = to_jpeg(frame_bgr)
                    state.latest_annotated_jpg = to_jpeg(annotated)
                    state.latest_result        = result_dict
                    state.history.append(result_dict)
                    if len(state.history) > MAX_HISTORY:
                        state.history.pop(0)

                    state.total_frames += 1
                    if new_event:
                        state.total_detections += len(event_detections)

                    state.fps = round(1000.0 / max(latency_ms, 1), 2)

                previous_frame_had_animal = animal_present

            else:
                # Idle mode: live raw frame only, no YOLO
                with state.lock:
                    state.latest_frame_jpg = to_jpeg(frame_bgr)
                    state.latest_annotated_jpg = to_jpeg(frame_bgr)
                    if state.latest_result is None:
                        state.latest_result = {
                            "timestamp": datetime.now().isoformat(),
                            "animal_present": False,
                            "detections": [],
                            "latency_ms": 0,
                            "frame_count": state.total_frames,
                            "motion_pct": round(motion_pct, 2),
                        }

                previous_frame_had_animal = False

            prev_gray = gray_blur

        except Exception as e:
            print(f"Detection error: {e}")
            import traceback
            traceback.print_exc()

        elapsed = time.time() - loop_start
        time.sleep(max(0, 0.03 - elapsed))  # ~30 FPS target for idle/live loop

    camera.stop()
    print("Detection loop stopped")

def start_detection():
    thread = threading.Thread(target=detection_loop, daemon=True)
    thread.start()
    return thread