# api/main.py
import io
import time
from datetime import datetime
from pathlib import Path

import cv2
import numpy as np
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from PIL import Image
from ultralytics import YOLO

app = FastAPI(title="WildTrack AI API", version="2.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Config ────────────────────────────────────────────────────────────────────
MODEL_PATH = "best.pt"
CONF_THRESHOLD = 0.35
IMG_SIZE = 640

LEGALITY = {
    "deer":     "legal",
    "boar":     "legal",
    "rabbit":   "legal",
    "pheasant": "legal",
    "jackal":   "illegal",
}

# ── Load model once at startup ─────────────────────────────────────────────────
model = None

@app.on_event("startup")
async def startup():
    global model
    model = YOLO(MODEL_PATH)
    print(f"✓ Model loaded from {MODEL_PATH}")

# ── Preprocessing — exactly matches training pipeline ─────────────────────────
def preprocess(image_bytes: bytes) -> np.ndarray:
    """
    Preprocess image exactly like our training data:
    1. Decode image
    2. Resize to 640x640
    3. Apply CLAHE normalization (same as training)
    """
    # Decode
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    if img is None:
        raise ValueError("Could not decode image")

    # Resize to 640x640
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))

    # Apply CLAHE — exactly as done during dataset preparation
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    l = clahe.apply(l)
    lab = cv2.merge([l, a, b])
    img = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

    return img

# ── Health check ───────────────────────────────────────────────────────────────
@app.get("/health")
def health():
    return {
        "status": "ok",
        "model_loaded": model is not None,
        "model_path": MODEL_PATH,
        "confidence_threshold": CONF_THRESHOLD
    }

# ── Classes ────────────────────────────────────────────────────────────────────
@app.get("/classes")
def get_classes():
    return {
        "species": list(LEGALITY.keys()),
        "legality": LEGALITY
    }

# ── Main detection endpoint ────────────────────────────────────────────────────
@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    """
    Detect wildlife in uploaded image.
    Applies same preprocessing as training data for maximum confidence.
    """
    if model is None:
        return JSONResponse(status_code=503, content={"error": "Model not loaded"})

    # Read image bytes
    image_bytes = await file.read()

    # Preprocess — same as training pipeline
    try:
        img_processed = preprocess(image_bytes)
    except Exception as e:
        return JSONResponse(status_code=400, content={"error": str(e)})

    # Run inference
    t0 = time.time()
    results = model.predict(
        source  = img_processed,
        conf    = CONF_THRESHOLD,
        verbose = False
    )
    latency_ms = round((time.time() - t0) * 1000, 1)

    result = results[0]
    detections = []
    privacy_alert = False

    for box in result.boxes:
        class_id   = int(box.cls[0])
        confidence = float(box.conf[0])
        species    = model.names.get(class_id, "unknown")
        bbox       = [round(v, 1) for v in box.xyxy[0].tolist()]
        legal      = LEGALITY.get(species, "illegal")

        if species == "human":
            privacy_alert = True

        detections.append({
            "species":    species,
            "confidence": round(confidence, 4),
            "bbox":       bbox,
            "legal":      legal
        })

    return {
        "image":          file.filename,
        "animal_present": len(detections) > 0,
        "detections":     detections,
        "privacy_alert":  privacy_alert,
        "timestamp":      datetime.now().isoformat(),
        "latency_ms":     latency_ms,
        "empty_frame":    len(detections) == 0
    }

# ── Batch detection ────────────────────────────────────────────────────────────
@app.post("/detect/batch")
async def detect_batch(files: list[UploadFile] = File(...)):
    """Detect wildlife in multiple images."""
    if len(files) > 50:
        return JSONResponse(status_code=400, content={"error": "Max 50 images per batch"})

    results_out = []
    for file in files:
        image_bytes = await file.read()
        try:
            img_processed = preprocess(image_bytes)
        except Exception as e:
            results_out.append({"image": file.filename, "error": str(e)})
            continue

        results = model.predict(img_processed, conf=CONF_THRESHOLD, verbose=False)
        result  = results[0]
        detections = []

        for box in result.boxes:
            class_id   = int(box.cls[0])
            confidence = float(box.conf[0])
            species    = model.names.get(class_id, "unknown")
            legal      = LEGALITY.get(species, "illegal")

            detections.append({
                "species":    species,
                "confidence": round(confidence, 4),
                "bbox":       [round(v, 1) for v in box.xyxy[0].tolist()],
                "legal":      legal
            })

        results_out.append({
            "image":          file.filename,
            "animal_present": len(detections) > 0,
            "detections":     detections,
            "timestamp":      datetime.now().isoformat(),
            "empty_frame":    len(detections) == 0
        })

    return {
        "results": results_out,
        "total":   len(results_out),
        "animals_found": sum(1 for r in results_out if r.get("animal_present"))
    }
