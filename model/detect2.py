"""
model/detect.py
Motion-triggered live detection window.

Behavior:
- Idle until motion is detected.
- Once motion is detected, opens a 5-second LIVE window.
- During the 5-second window, runs YOLO continuously and updates live feed.

Counting/logging rule (Approach B — per-species state machine):
  Each species moves through: unseen -> present -> cooling_down -> unseen
  - Logged exactly ONCE when transitioning unseen -> present.
  - Bounding boxes always draw regardless of state.
  - 10s cooldown starts when the animal DISAPPEARS from frame.
  - Same species cannot re-trigger until cooldown expires.
  - Different species are tracked independently.
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

MOTION_THRESHOLD   = 5.0
FRAME_DIFF_BLUR    = 21
LIVE_WINDOW_MS     = 5000

COOLDOWN_SECS      = 10.0   # starts when animal leaves frame, per species

MAX_HISTORY        = 50
SAVE_FRAMES        = True
FRAMES_DIR         = Path("frames")
DETECTION_LOG_TXT  = Path("detections.txt")
DETECTION_LOG_CSV  = Path("detections.csv")

LEGALITY = {
    "deer":     "legal",
    "boar":     "legal",
    "rabbit":   "legal",
    "pheasant": "legal",
    "jackal":   "illegal",
}

FRAMES_DIR.mkdir(exist_ok=True)

# ── Permanent detection log (txt + csv) ───────────────────────────────────────
_log_lock = threading.Lock()

def _init_logs():
    """Create log files with headers if they don't exist or are empty."""
    if not DETECTION_LOG_TXT.exists() or DETECTION_LOG_TXT.stat().st_size == 0:
        with open(DETECTION_LOG_TXT, "w", encoding="utf-8") as f:
            f.write("# WildTrack Hunt Log\n")
            f.write(f"# Created: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("# Format: timestamp | species | confidence | legal_status\n")
            f.write("#" + "-" * 60 + "\n")

    if not DETECTION_LOG_CSV.exists() or DETECTION_LOG_CSV.stat().st_size == 0:
        with open(DETECTION_LOG_CSV, "w", encoding="utf-8") as f:
            f.write("timestamp,species,confidence,legal_status\n")

def log_detection(timestamp: str, detection: dict):
    """Write one entry to both the .txt and .csv log files atomically."""
    species    = detection['species']
    confidence = detection['confidence']
    legal      = detection['legal']

    txt_line = (
        f"{timestamp} | {species:<10} | {confidence:.2%} | {legal}\n"
    )
    csv_line = (
        f"{timestamp},{species},{confidence:.4f},{legal}\n"
    )

    with _log_lock:
        with open(DETECTION_LOG_TXT, "a", encoding="utf-8") as f:
            f.write(txt_line)
        with open(DETECTION_LOG_CSV, "a", encoding="utf-8") as f:
            f.write(csv_line)

_init_logs()

# ── Shared state ───────────────────────────────────────────────────────────────
class DetectionState:
    def __init__(self):
        self.lock                 = threading.Lock()
        self.latest_frame_jpg     = None
        self.latest_annotated_jpg = None
        self.latest_result        = None
        self.history              = []
        self.running              = False
        self.fps                  = 0.0
        self.total_frames         = 0
        self.total_detections     = 0
        self.motion_state         = "idle"
        self.motion_pct           = 0.0

state = DetectionState()

# ── Per-species state machine (Approach B) ─────────────────────────────────────
class SpeciesTracker:
    """
    Tracks each species through three states:
      unseen       -> can trigger a new log event
      present      -> currently in frame, already logged, won't re-log
      cooling_down -> just left frame, cooldown timer running

    Cooldown starts on DISAPPEARANCE, not on first detection.
    A deer standing still for 60s is logged once and never re-logged.
    After it leaves, it can only re-trigger after COOLDOWN_SECS.
    """
    def __init__(self, cooldown_secs: float = COOLDOWN_SECS):
        self.cooldown_secs = cooldown_secs
        self._species: dict = {}   # species -> {state, cooldown_until}

    def _get(self, species: str) -> dict:
        if species not in self._species:
            self._species[species] = {"state": "unseen", "cooldown_until": 0.0}
        return self._species[species]

    def update(self, detected_species: set, now: float) -> list:
        """
        Call once per frame with the set of detected species.
        Returns list of species that are new events this frame (should be logged).
        """
        new_events = []

        # Handle species visible this frame
        for species in detected_species:
            entry = self._get(species)
            if entry["state"] == "unseen":
                entry["state"] = "present"
                new_events.append(species)
            elif entry["state"] == "cooling_down":
                if now >= entry["cooldown_until"]:
                    # Cooldown expired — fresh event
                    entry["state"] = "present"
                    new_events.append(species)
                else:
                    # Reappeared mid-cooldown — mark present, don't log
                    entry["state"] = "present"
            # "present" -> already logged, nothing to do

        # Handle species NOT visible this frame
        for species in set(self._species.keys()) - detected_species:
            entry = self._get(species)
            if entry["state"] == "present":
                # Just left frame — start cooldown
                entry["state"] = "cooling_down"
                entry["cooldown_until"] = now + self.cooldown_secs
            elif entry["state"] == "cooling_down":
                if now >= entry["cooldown_until"]:
                    entry["state"] = "unseen"

        return new_events

    def reset(self):
        self._species.clear()


# ── Helpers ────────────────────────────────────────────────────────────────────
def to_jpeg(img_bgr):
    _, buf = cv2.imencode(".jpg", img_bgr, [cv2.IMWRITE_JPEG_QUALITY, 85])
    return buf.tobytes()

def compute_motion(prev_gray, curr_gray):
    diff = cv2.absdiff(prev_gray, curr_gray)
    _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
    return (np.sum(thresh > 0) / thresh.size) * 100.0

def run_inference(model, frame_bgr):
    """
    Run YOLO and draw bounding boxes.
    Boxes are ALWAYS drawn — cooldown never affects the visual output.
    """
    results = model.predict(
        source=frame_bgr,
        conf=CONF_THRESHOLD,
        verbose=False,
        imgsz=IMG_SIZE,
    )
    result   = results[0]
    detections = []
    annotated  = frame_bgr.copy()

    for box in result.boxes:
        x1, y1, x2, y2 = box.xyxy[0].tolist()
        if (x2 - x1) * (y2 - y1) < MIN_BOX_AREA:
            continue

        class_id   = int(box.cls[0])
        confidence = float(box.conf[0])
        species    = model.names.get(class_id, "unknown")
        legal      = LEGALITY.get(species, "illegal")

        detections.append({
            "species":    species,
            "confidence": round(confidence, 4),
            "bbox":       [round(v, 1) for v in [x1, y1, x2, y2]],
            "legal":      legal,
        })

        color = (0, 255, 127) if legal == "legal" else (82, 82, 224)
        cv2.rectangle(annotated, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)
        cv2.putText(
            annotated, f"{species} {confidence:.0%}",
            (int(x1), max(int(y1) - 8, 15)),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2,
        )

    return detections, annotated

def dedupe_by_species(detections: list) -> dict:
    """Return {species: best_detection} keeping highest confidence per species."""
    best: dict = {}
    for det in detections:
        sp = det["species"]
        if sp not in best or det["confidence"] > best[sp]["confidence"]:
            best[sp] = det
    return best

# ── Main detection loop ────────────────────────────────────────────────────────
def detection_loop():
    print("Loading model...")
    model = YOLO(MODEL_PATH)
    print(f"  Model loaded: {MODEL_PATH}")

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
    print("Camera ready — MOTION -> 5s LIVE WINDOW mode")
    print(f"  Motion threshold : {MOTION_THRESHOLD}%")
    print(f"  Live window      : {LIVE_WINDOW_MS}ms")
    print(f"  Cooldown         : {COOLDOWN_SECS}s per species (starts on disappearance)")
    print(f"  Log (txt)        : {DETECTION_LOG_TXT.absolute()}\n"
    f"  Log (csv)        : {DETECTION_LOG_CSV.absolute()}")

    state.running  = True
    prev_gray      = None
    live_until_ms  = 0
    tracker        = SpeciesTracker()

    while state.running:
        loop_start = time.time()

        try:
            frame_rgb  = camera.capture_array("main")
            frame_bgr  = frame_rgb   # imx708_wide outputs BGR despite RGB888 label

            gray       = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2GRAY)
            gray_blur  = cv2.GaussianBlur(gray, (FRAME_DIFF_BLUR, FRAME_DIFF_BLUR), 0)

            now_ms     = time.time() * 1000
            now_secs   = now_ms / 1000.0
            motion_pct = 0.0

            if prev_gray is not None:
                motion_pct = compute_motion(prev_gray, gray_blur)

            if motion_pct > MOTION_THRESHOLD:
                if now_ms >= live_until_ms:
                    # Fresh trigger — reset tracker for new window
                    tracker.reset()
                    print(f"Motion detected: {motion_pct:.1f}% — LIVE for 5s")
                # Always extend window while motion continues
                live_until_ms = now_ms + LIVE_WINDOW_MS

            in_live_window = now_ms < live_until_ms

            with state.lock:
                state.motion_pct   = round(motion_pct, 2)
                state.motion_state = "detected" if in_live_window else "idle"

            if in_live_window:
                t0 = time.time()
                detections, annotated = run_inference(model, frame_bgr)
                latency_ms     = round((time.time() - t0) * 1000, 1)
                animal_present = len(detections) > 0

                # State machine — returns species that are genuine new events
                detected_species  = {d["species"] for d in detections}
                new_event_species = tracker.update(detected_species, now_secs)

                if new_event_species:
                    best            = dedupe_by_species(detections)
                    ts_readable     = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    for sp in new_event_species:
                        det = best.get(sp)
                        if det:
                            log_detection(ts_readable, det)
                            print(
                                f"  New event: {det['species']} "
                                f"({det['confidence']:.0%}) [{det['legal']}]"
                            )

                timestamp   = datetime.now().isoformat()
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
                    if new_event_species:
                        state.total_detections += len(new_event_species)
                    state.fps = round(1000.0 / max(latency_ms, 1), 2)

            else:
                # Idle — reset tracker so next window starts clean
                tracker.reset()

                with state.lock:
                    state.latest_frame_jpg     = to_jpeg(frame_bgr)
                    state.latest_annotated_jpg = to_jpeg(frame_bgr)
                    if state.latest_result is None:
                        state.latest_result = {
                            "timestamp":     datetime.now().isoformat(),
                            "animal_present": False,
                            "detections":    [],
                            "latency_ms":    0,
                            "frame_count":   state.total_frames,
                            "motion_pct":    round(motion_pct, 2),
                        }

            prev_gray = gray_blur

        except Exception as e:
            print(f"Detection error: {e}")
            import traceback
            traceback.print_exc()

        elapsed = time.time() - loop_start
        time.sleep(max(0, 0.03 - elapsed))  # ~30 FPS target

    camera.stop()
    print("Detection loop stopped")


def start_detection():
    thread = threading.Thread(target=detection_loop, daemon=True)
    thread.start()
    return thread
