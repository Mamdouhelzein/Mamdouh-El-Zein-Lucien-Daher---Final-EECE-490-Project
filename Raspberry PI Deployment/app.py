
Gemini

Generate your next big idea with Gemini in Gmail, Docs, and more
Power up your productivity with AI features directly in the apps you use every day

Create drafts in Docs

Plan projects quickly in Sheets

Generate original images in Slides

Start enhanced meetings in Meet
Plus, get access to Gemini Pro with our most capable AI models and more storage
Already signed up? Refresh this page
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>WildTrack AI — Wildlife Detection System</title>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:wght@400;500&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
<style>
  :root {
    --forest:    #0d1f0f;
    --canopy:    #1a3320;
    --moss:      #2d5a3d;
    --fern:      #4a8c5c;
    --leaf:      #6dbf7e;
    --mist:      #e8f3e8;
    --bark:      #8b6f47;
    --amber:     #f0a500;
    --danger:    #e05252;
    --safe:      #4caf7d;
    --text:      #e8f3e8;
    --text-dim:  #7aab82;
    --card-bg:   rgba(26, 51, 32, 0.7);
    --border:    rgba(77, 140, 92, 0.25);
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    font-family: 'DM Sans', sans-serif;
    background: var(--forest);
    color: var(--text);
    min-height: 100vh;
    overflow-x: hidden;
  }

  /* Animated forest background */
  body::before {
    content: '';
    position: fixed;
    inset: 0;
    background:
      radial-gradient(ellipse 80% 60% at 20% 0%, rgba(45, 90, 61, 0.4) 0%, transparent 60%),
      radial-gradient(ellipse 60% 80% at 80% 100%, rgba(13, 31, 15, 0.8) 0%, transparent 60%),
      radial-gradient(ellipse 40% 40% at 50% 50%, rgba(26, 51, 32, 0.3) 0%, transparent 70%);
    pointer-events: none;
    z-index: 0;
  }

  /* Noise texture overlay */
  body::after {
    content: '';
    position: fixed;
    inset: 0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.04'/%3E%3C/svg%3E");
    opacity: 0.4;
    pointer-events: none;
    z-index: 0;
  }

  .container {
    position: relative;
    z-index: 1;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
  }

  /* ── Header ── */
  header {
    padding: 2.5rem 0 2rem;
    border-bottom: 1px solid var(--border);
  }

  .header-inner {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .logo {
    display: flex;
    align-items: center;
    gap: 1rem;
  }

  .logo-icon {
    width: 48px;
    height: 48px;
    background: linear-gradient(135deg, var(--fern), var(--leaf));
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.5rem;
    box-shadow: 0 4px 20px rgba(77, 140, 92, 0.4);
  }

  .logo-text h1 {
    font-family: 'Syne', sans-serif;
    font-size: 1.6rem;
    font-weight: 800;
    letter-spacing: -0.03em;
    color: var(--mist);
  }

  .logo-text p {
    font-size: 0.8rem;
    color: var(--text-dim);
    font-family: 'DM Mono', monospace;
    letter-spacing: 0.05em;
  }

  .header-stats {
    display: flex;
    gap: 2rem;
  }

  .stat {
    text-align: right;
  }

  .stat-value {
    font-family: 'Syne', sans-serif;
    font-size: 1.4rem;
    font-weight: 700;
    color: var(--leaf);
  }

  .stat-label {
    font-size: 0.75rem;
    color: var(--text-dim);
    font-family: 'DM Mono', monospace;
  }

  /* ── Main layout ── */
  .main {
    padding: 3rem 0;
    display: grid;
    grid-template-columns: 1fr 1.4fr;
    gap: 2rem;
    align-items: start;
  }

  /* ── Upload panel ── */
  .panel {
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 1.8rem;
    backdrop-filter: blur(12px);
  }

  .panel-title {
    font-family: 'Syne', sans-serif;
    font-size: 1rem;
    font-weight: 700;
    color: var(--text-dim);
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 1.2rem;
  }

  .drop-zone {
    border: 2px dashed var(--border);
    border-radius: 16px;
    padding: 3rem 2rem;
    text-align: center;
    cursor: pointer;
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
  }

  .drop-zone::before {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse at center, rgba(77, 140, 92, 0.08) 0%, transparent 70%);
    opacity: 0;
    transition: opacity 0.3s;
  }

  .drop-zone:hover::before,
  .drop-zone.dragover::before { opacity: 1; }

  .drop-zone:hover,
  .drop-zone.dragover {
    border-color: var(--fern);
    background: rgba(77, 140, 92, 0.05);
  }

  .drop-icon {
    font-size: 3rem;
    margin-bottom: 1rem;
    display: block;
  }

  .drop-zone h3 {
    font-family: 'Syne', sans-serif;
    font-size: 1.1rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
  }

  .drop-zone p {
    font-size: 0.85rem;
    color: var(--text-dim);
  }

  .drop-zone input[type="file"] {
    position: absolute;
    inset: 0;
    opacity: 0;
    cursor: pointer;
  }

  /* Preview grid */
  .preview-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 0.6rem;
    margin-top: 1.2rem;
  }

  .preview-item {
    aspect-ratio: 1;
    border-radius: 10px;
    overflow: hidden;
    position: relative;
    border: 1px solid var(--border);
  }

  .preview-item img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  .preview-item .remove-btn {
    position: absolute;
    top: 4px;
    right: 4px;
    background: rgba(0,0,0,0.7);
    border: none;
    color: white;
    width: 20px;
    height: 20px;
    border-radius: 50%;
    cursor: pointer;
    font-size: 0.7rem;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  /* Settings */
  .settings {
    margin-top: 1.5rem;
  }

  .setting-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.8rem 0;
    border-bottom: 1px solid var(--border);
  }

  .setting-row:last-child { border-bottom: none; }

  .setting-label {
    font-size: 0.85rem;
    color: var(--text-dim);
    font-family: 'DM Mono', monospace;
  }

  .setting-value {
    font-family: 'DM Mono', monospace;
    font-size: 0.9rem;
    color: var(--leaf);
    font-weight: 500;
  }

  input[type="range"] {
    -webkit-appearance: none;
    width: 120px;
    height: 4px;
    background: var(--canopy);
    border-radius: 2px;
    outline: none;
  }

  input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    width: 16px;
    height: 16px;
    background: var(--leaf);
    border-radius: 50%;
    cursor: pointer;
    box-shadow: 0 0 8px rgba(109, 191, 126, 0.5);
  }

  /* Detect button */
  .detect-btn {
    width: 100%;
    padding: 1rem;
    margin-top: 1.5rem;
    background: linear-gradient(135deg, var(--fern), var(--leaf));
    border: none;
    border-radius: 12px;
    color: var(--forest);
    font-family: 'Syne', sans-serif;
    font-size: 1rem;
    font-weight: 700;
    cursor: pointer;
    letter-spacing: 0.02em;
    transition: all 0.3s ease;
    box-shadow: 0 4px 20px rgba(77, 140, 92, 0.3);
    position: relative;
    overflow: hidden;
  }

  .detect-btn::before {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, rgba(255,255,255,0.1), transparent);
    opacity: 0;
    transition: opacity 0.3s;
  }

  .detect-btn:hover::before { opacity: 1; }
  .detect-btn:hover { transform: translateY(-2px); box-shadow: 0 8px 30px rgba(77, 140, 92, 0.4); }
  .detect-btn:active { transform: translateY(0); }
  .detect-btn:disabled { opacity: 0.5; cursor: not-allowed; transform: none; }

  /* Loading */
  .loading {
    display: none;
    align-items: center;
    gap: 0.8rem;
    padding: 1rem;
    background: rgba(77, 140, 92, 0.1);
    border-radius: 10px;
    margin-top: 1rem;
  }

  .loading.active { display: flex; }

  .spinner {
    width: 20px;
    height: 20px;
    border: 2px solid var(--border);
    border-top-color: var(--leaf);
    border-radius: 50%;
    animation: spin 0.8s linear infinite;
  }

  @keyframes spin { to { transform: rotate(360deg); } }

  .loading-text {
    font-family: 'DM Mono', monospace;
    font-size: 0.85rem;
    color: var(--text-dim);
  }

  /* ── Results panel ── */
  .results-panel {
    display: flex;
    flex-direction: column;
    gap: 1.2rem;
  }

  .empty-state {
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 4rem 2rem;
    text-align: center;
    backdrop-filter: blur(12px);
  }

  .empty-state .empty-icon {
    font-size: 4rem;
    margin-bottom: 1rem;
    opacity: 0.4;
  }

  .empty-state p {
    color: var(--text-dim);
    font-size: 0.9rem;
  }

  /* Result card */
  .result-card {
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 20px;
    overflow: hidden;
    backdrop-filter: blur(12px);
    animation: slideIn 0.4s ease;
  }

  @keyframes slideIn {
    from { opacity: 0; transform: translateY(10px); }
    to   { opacity: 1; transform: translateY(0); }
  }

  .result-images {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0;
  }

  .result-img-wrap {
    position: relative;
    aspect-ratio: 4/3;
    overflow: hidden;
  }

  .result-img-wrap img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  .result-img-label {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    padding: 0.4rem 0.8rem;
    background: linear-gradient(transparent, rgba(0,0,0,0.7));
    font-family: 'DM Mono', monospace;
    font-size: 0.7rem;
    color: rgba(255,255,255,0.7);
  }

  .result-body {
    padding: 1.2rem 1.5rem;
  }

  .result-filename {
    font-family: 'DM Mono', monospace;
    font-size: 0.75rem;
    color: var(--text-dim);
    margin-bottom: 0.8rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .empty-badge {
    background: rgba(255,255,255,0.08);
    padding: 0.25rem 0.6rem;
    border-radius: 6px;
    font-size: 0.7rem;
    color: var(--text-dim);
  }

  /* Detection item */
  .detection-item {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0.7rem 0.9rem;
    background: rgba(13, 31, 15, 0.5);
    border-radius: 10px;
    margin-bottom: 0.5rem;
    border: 1px solid var(--border);
  }

  .detection-left {
    display: flex;
    align-items: center;
    gap: 0.8rem;
  }

  .species-icon {
    font-size: 1.4rem;
  }

  .species-name {
    font-family: 'Syne', sans-serif;
    font-size: 0.95rem;
    font-weight: 700;
    text-transform: capitalize;
  }

  .species-conf {
    font-family: 'DM Mono', monospace;
    font-size: 0.75rem;
    color: var(--text-dim);
    margin-top: 0.1rem;
  }

  .conf-bar {
    width: 60px;
    height: 3px;
    background: var(--canopy);
    border-radius: 2px;
    margin-top: 0.3rem;
    overflow: hidden;
  }

  .conf-fill {
    height: 100%;
    border-radius: 2px;
    background: linear-gradient(90deg, var(--fern), var(--leaf));
    transition: width 0.5s ease;
  }

  .legal-badge {
    padding: 0.3rem 0.7rem;
    border-radius: 8px;
    font-family: 'DM Mono', monospace;
    font-size: 0.75rem;
    font-weight: 500;
  }

  .legal-badge.legal {
    background: rgba(76, 175, 125, 0.15);
    color: var(--safe);
    border: 1px solid rgba(76, 175, 125, 0.3);
  }

  .legal-badge.illegal {
    background: rgba(224, 82, 82, 0.15);
    color: var(--danger);
    border: 1px solid rgba(224, 82, 82, 0.3);
  }

  /* Summary bar */
  .summary-bar {
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 1.2rem 1.5rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    backdrop-filter: blur(12px);
  }

  .summary-stat {
    text-align: center;
  }

  .summary-num {
    font-family: 'Syne', sans-serif;
    font-size: 1.8rem;
    font-weight: 800;
    color: var(--leaf);
    line-height: 1;
  }

  .summary-lbl {
    font-size: 0.72rem;
    color: var(--text-dim);
    font-family: 'DM Mono', monospace;
    margin-top: 0.2rem;
  }

  /* CSV button */
  .csv-btn {
    padding: 0.6rem 1.2rem;
    background: transparent;
    border: 1px solid var(--border);
    border-radius: 10px;
    color: var(--text-dim);
    font-family: 'DM Mono', monospace;
    font-size: 0.8rem;
    cursor: pointer;
    transition: all 0.2s;
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }

  .csv-btn:hover {
    border-color: var(--fern);
    color: var(--leaf);
    background: rgba(77, 140, 92, 0.05);
  }

  /* API status */
  .api-status {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-family: 'DM Mono', monospace;
    font-size: 0.75rem;
    color: var(--text-dim);
  }

  .status-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: var(--text-dim);
  }

  .status-dot.online { background: var(--safe); box-shadow: 0 0 6px var(--safe); animation: pulse 2s infinite; }
  .status-dot.offline { background: var(--danger); }

  @keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.5; }
  }

  /* Toast */
  .toast {
    position: fixed;
    bottom: 2rem;
    right: 2rem;
    background: var(--canopy);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 0.8rem 1.2rem;
    font-family: 'DM Mono', monospace;
    font-size: 0.8rem;
    color: var(--text);
    z-index: 100;
    transform: translateY(100px);
    opacity: 0;
    transition: all 0.3s ease;
  }

  .toast.show { transform: translateY(0); opacity: 1; }

  /* Scrollbar */
  ::-webkit-scrollbar { width: 6px; }
  ::-webkit-scrollbar-track { background: var(--forest); }
  ::-webkit-scrollbar-thumb { background: var(--moss); border-radius: 3px; }

  /* Species icons map */
  .icon-deer     { content: '🦌'; }
  .icon-boar     { content: '🐗'; }
  .icon-rabbit   { content: '🐇'; }
  .icon-jackal   { content: '🐺'; }
  .icon-pheasant { content: '🦃'; }

  @media (max-width: 900px) {
    .main { grid-template-columns: 1fr; }
    .header-stats { display: none; }
  }
</style>
</head>
<body>

<div class="container">
  <!-- Header -->
  <header>
    <div class="header-inner">
      <div class="logo">
        <div class="logo-icon">🌲</div>
        <div class="logo-text">
          <h1>WildTrack AI</h1>
          <p>TRAIL CAMERA DETECTION SYSTEM</p>
        </div>
      </div>
      <div class="header-stats">
        <div class="stat">
          <div class="stat-value">0.948</div>
          <div class="stat-label">mAP@0.5</div>
        </div>
        <div class="stat">
          <div class="stat-value">5</div>
          <div class="stat-label">SPECIES</div>
        </div>
        <div class="api-status">
          <div class="status-dot" id="statusDot"></div>
          <span id="statusText">checking api...</span>
        </div>
      </div>
    </div>
  </header>

  <!-- Main -->
  <div class="main">
    <!-- Left: Upload + Settings -->
    <div>
      <div class="panel">
        <div class="panel-title">Upload Images</div>

        <div class="drop-zone" id="dropZone">
          <input type="file" id="fileInput" accept="image/*" multiple>
          <span class="drop-icon">📷</span>
          <h3>Drop trail cam images here</h3>
          <p>JPG, PNG, WEBP supported · Multiple files</p>
        </div>

        <div class="preview-grid" id="previewGrid"></div>

        <div class="settings">
          <div class="panel-title" style="margin-top:1.2rem;">Settings</div>

          <div class="setting-row">
            <span class="setting-label">confidence threshold</span>
            <div style="display:flex;align-items:center;gap:0.8rem;">
              <input type="range" id="confSlider" min="0.1" max="0.9" step="0.01" value="0.35">
              <span class="setting-value" id="confValue">0.35</span>
            </div>
          </div>

          <div class="setting-row">
            <span class="setting-label">api endpoint</span>
            <input id="apiUrl" value="http://localhost:8000" 
              style="background:transparent;border:none;color:var(--leaf);font-family:'DM Mono',monospace;font-size:0.8rem;text-align:right;outline:none;width:180px;">
          </div>

          <div class="setting-row">
            <span class="setting-label">model</span>
            <span class="setting-value">YOLOv8n · forest_lens_v2</span>
          </div>
        </div>

        <button class="detect-btn" id="detectBtn" onclick="runDetection()">
          ⚡ Run Detection
        </button>

        <div class="loading" id="loading">
          <div class="spinner"></div>
          <span class="loading-text" id="loadingText">Processing images...</span>
        </div>
      </div>
    </div>

    <!-- Right: Results -->
    <div class="results-panel" id="resultsPanel">
      <div class="empty-state" id="emptyState">
        <div class="empty-icon">🌿</div>
        <p>Upload trail camera images and run detection<br>to see results here</p>
      </div>
    </div>
  </div>
</div>

<div class="toast" id="toast"></div>

<script>
  const SPECIES_ICONS = {
    deer: '🦌', boar: '🐗', rabbit: '🐇',
    jackal: '🐺', pheasant: '🦃', unknown: '❓'
  };

  let selectedFiles = [];
  let allResults = [];
  let totalDetections = 0;
  let totalAnimals = 0;
  let totalEmpty = 0;

  // ── API status check ───────────────────────────────────────────────────────
  async function checkApi() {
    const dot = document.getElementById('statusDot');
    const txt = document.getElementById('statusText');
    try {
      const r = await fetch(`${document.getElementById('apiUrl').value}/health`, {signal: AbortSignal.timeout(3000)});
      if (r.ok) {
        dot.className = 'status-dot online';
        txt.textContent = 'api online';
      } else throw new Error();
    } catch {
      dot.className = 'status-dot offline';
      txt.textContent = 'api offline';
    }
  }

  checkApi();
  setInterval(checkApi, 10000);

  // ── File handling ──────────────────────────────────────────────────────────
  const dropZone = document.getElementById('dropZone');
  const fileInput = document.getElementById('fileInput');

  dropZone.addEventListener('dragover', e => { e.preventDefault(); dropZone.classList.add('dragover'); });
  dropZone.addEventListener('dragleave', () => dropZone.classList.remove('dragover'));
  dropZone.addEventListener('drop', e => {
    e.preventDefault();
    dropZone.classList.remove('dragover');
    addFiles([...e.dataTransfer.files]);
  });

  fileInput.addEventListener('change', () => addFiles([...fileInput.files]));

  function addFiles(files) {
    const imageFiles = files.filter(f => f.type.startsWith('image/'));
    selectedFiles = [...selectedFiles, ...imageFiles];
    renderPreviews();
  }

  function renderPreviews() {
    const grid = document.getElementById('previewGrid');
    grid.innerHTML = '';
    selectedFiles.forEach((file, i) => {
      const url = URL.createObjectURL(file);
      const item = document.createElement('div');
      item.className = 'preview-item';
      item.innerHTML = `
        <img src="${url}" alt="${file.name}">
        <button class="remove-btn" onclick="removeFile(${i})">✕</button>
      `;
      grid.appendChild(item);
    });
  }

  function removeFile(index) {
    selectedFiles.splice(index, 1);
    renderPreviews();
  }

  // ── Confidence slider ──────────────────────────────────────────────────────
  document.getElementById('confSlider').addEventListener('input', function() {
    document.getElementById('confValue').textContent = parseFloat(this.value).toFixed(2);
  });

  // ── Detection ──────────────────────────────────────────────────────────────
  async function runDetection() {
    if (selectedFiles.length === 0) { showToast('Upload at least one image first'); return; }

    const apiUrl = document.getElementById('apiUrl').value;
    const conf   = document.getElementById('confSlider').value;
    const btn    = document.getElementById('detectBtn');
    const loading = document.getElementById('loading');

    btn.disabled = true;
    loading.classList.add('active');
    allResults = [];
    totalDetections = 0;
    totalAnimals = 0;
    totalEmpty = 0;

    // Clear results
    const panel = document.getElementById('resultsPanel');
    panel.innerHTML = '';
    document.getElementById('emptyState') && panel.appendChild(Object.assign(document.createElement('div'), {id: 'emptyState'}));

    for (let i = 0; i < selectedFiles.length; i++) {
      const file = selectedFiles[i];
      document.getElementById('loadingText').textContent = `Processing ${i+1}/${selectedFiles.length}: ${file.name}`;

      try {
        const formData = new FormData();
        formData.append('file', file);

        const response = await fetch(`${apiUrl}/detect?conf=${conf}`, {
          method: 'POST',
          body: formData
        });

        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        const result = await response.json();

        allResults.push({file, result});
        totalDetections += result.detections?.length || 0;
        if (result.animal_present) totalAnimals++;
        else totalEmpty++;

        renderResult(file, result, panel);

      } catch (err) {
        renderError(file, err.message, panel);
      }
    }

    // Summary
    renderSummary(panel);

    btn.disabled = false;
    loading.classList.remove('active');
    showToast(`✓ Processed ${selectedFiles.length} images`);
  }

  // ── Render result card ─────────────────────────────────────────────────────
  function renderResult(file, result, panel) {
    const card = document.createElement('div');
    card.className = 'result-card';

    const originalUrl = URL.createObjectURL(file);

    // Build detections HTML
    let detectionsHtml = '';
    if (!result.animal_present || !result.detections?.length) {
      detectionsHtml = `<div style="text-align:center;padding:1rem;color:var(--text-dim);font-family:'DM Mono',monospace;font-size:0.8rem;">
        🌿 No animals detected — empty frame filtered
      </div>`;
    } else {
      result.detections.forEach(d => {
        const icon = SPECIES_ICONS[d.species] || '❓';
        const confPct = Math.round(d.confidence * 100);
        const legalClass = d.legal === 'legal' ? 'legal' : 'illegal';
        const legalIcon  = d.legal === 'legal' ? '✅' : '⛔';
        detectionsHtml += `
          <div class="detection-item">
            <div class="detection-left">
              <span class="species-icon">${icon}</span>
              <div>
                <div class="species-name">${d.species}</div>
                <div class="species-conf">${confPct}% confidence</div>
                <div class="conf-bar"><div class="conf-fill" style="width:${confPct}%"></div></div>
              </div>
            </div>
            <span class="legal-badge ${legalClass}">${legalIcon} ${d.legal}</span>
          </div>`;
      });
    }

    card.innerHTML = `
      <div class="result-images">
        <div class="result-img-wrap">
          <img src="${originalUrl}" alt="Original">
          <div class="result-img-label">Original</div>
        </div>
        <div class="result-img-wrap" id="annotated-${file.name.replace(/\W/g,'_')}">
          <img src="${originalUrl}" alt="Detection" style="filter:${result.animal_present ? 'none' : 'brightness(0.6)'}">
          <div class="result-img-label">Detection output</div>
        </div>
      </div>
      <div class="result-body">
        <div class="result-filename">
          <span>${file.name}</span>
          <span>${result.timestamp?.slice(0,19) || ''}</span>
        </div>
        ${detectionsHtml}
        ${result.privacy_alert ? `<div style="margin-top:0.5rem;padding:0.5rem 0.8rem;background:rgba(224,82,82,0.1);border-radius:8px;font-size:0.8rem;color:var(--danger);">⚠️ Human detected — privacy alert</div>` : ''}
      </div>`;

    panel.appendChild(card);
  }

  function renderError(file, message, panel) {
    const card = document.createElement('div');
    card.className = 'result-card';
    card.innerHTML = `<div class="result-body">
      <div class="result-filename">${file.name}</div>
      <div style="color:var(--danger);font-family:'DM Mono',monospace;font-size:0.8rem;">Error: ${message}</div>
    </div>`;
    panel.appendChild(card);
  }

  function renderSummary(panel) {
    const bar = document.createElement('div');
    bar.className = 'summary-bar';
    bar.innerHTML = `
      <div class="summary-stat">
        <div class="summary-num">${selectedFiles.length}</div>
        <div class="summary-lbl">images processed</div>
      </div>
      <div class="summary-stat">
        <div class="summary-num">${totalAnimals}</div>
        <div class="summary-lbl">with animals</div>
      </div>
      <div class="summary-stat">
        <div class="summary-num">${totalEmpty}</div>
        <div class="summary-lbl">empty filtered</div>
      </div>
      <div class="summary-stat">
        <div class="summary-num">${totalDetections}</div>
        <div class="summary-lbl">total detections</div>
      </div>
      <button class="csv-btn" onclick="downloadCSV()">⬇ Export CSV</button>
    `;
    panel.insertBefore(bar, panel.firstChild);
  }

  // ── CSV Export ─────────────────────────────────────────────────────────────
  function downloadCSV() {
    const rows = [['image', 'species', 'confidence', 'legal_status', 'timestamp', 'x1', 'y1', 'x2', 'y2']];
    allResults.forEach(({file, result}) => {
      if (!result.detections?.length) {
        rows.push([file.name, 'none', '', 'empty_frame', result.timestamp || '', '', '', '', '']);
      } else {
        result.detections.forEach(d => {
          rows.push([file.name, d.species, d.confidence, d.legal, result.timestamp || '',
            d.bbox?.[0]||'', d.bbox?.[1]||'', d.bbox?.[2]||'', d.bbox?.[3]||'']);
        });
      }
    });
    const csv = rows.map(r => r.join(',')).join('\n');
    const blob = new Blob([csv], {type: 'text/csv'});
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = `wildtrack_${new Date().toISOString().slice(0,10)}.csv`;
    a.click();
    showToast('CSV downloaded');
  }

  // ── Toast ──────────────────────────────────────────────────────────────────
  function showToast(msg) {
    const toast = document.getElementById('toast');
    toast.textContent = msg;
    toast.classList.add('show');
    setTimeout(() => toast.classList.remove('show'), 3000);
  }
</script>
</body>
</html>
