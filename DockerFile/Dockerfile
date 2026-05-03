# ─── WildTrack AI — Dockerized Upload API ──────────────────────────────────────
# Lightweight Python image — slim variant keeps the final image around 1.2 GB
# instead of 2+ GB with the default python:3.11 image.

FROM python:3.11-slim

# ── System dependencies ──────────────────────────────────────────────────────
# OpenCV needs libgl1 and libglib2.0-0 to load images at runtime.
# We use --no-install-recommends to avoid pulling in unnecessary packages.
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# ── Working directory ────────────────────────────────────────────────────────
WORKDIR /app

# ── Python dependencies ──────────────────────────────────────────────────────
# Copy requirements first so Docker can cache the pip install layer
# (it only re-runs when requirements.txt changes, not on every code change).
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# ── Application code ─────────────────────────────────────────────────────────
COPY api/  ./api/
COPY ui/   ./ui/
COPY best.pt .

# ── Runtime config ───────────────────────────────────────────────────────────
EXPOSE 8000

# Healthcheck so docker / orchestrators know if the API is alive
HEALTHCHECK --interval=30s --timeout=5s --start-period=15s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health', timeout=3)" || exit 1

# ── Entry point ──────────────────────────────────────────────────────────────
# --workers 1 because we have a single shared YOLO model in memory.
# Multiple workers would each load their own copy, eating RAM unnecessarily.
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]
