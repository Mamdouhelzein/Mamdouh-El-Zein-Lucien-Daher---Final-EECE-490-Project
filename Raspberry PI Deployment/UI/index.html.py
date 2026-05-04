
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
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>WildTrack — Trail Camera Intelligence</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600;700&family=Rubik:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<style>
  :root {
    --bg:          #141712;
    --bg-panel:    #1c201a;
    --bg-elevated: #232820;
    --bg-deep:     #0e100d;
    --forest:      #2d3b28;
    --moss:        #5a6e4a;
    --olive:       #7a8c4c;
    --khaki:       #a89968;
    --tan:         #c9a875;
    --bone:        #e8dfc7;
    --blood:       #8c3b2b;
    --rust:        #a64a2f;
    --amber:       #d49840;
    --danger:      #c23d2e;
    --safe:        #6b9447;
    --text:        #e8dfc7;
    --text-dim:    #8a8572;
    --text-faint:  #5a574c;
    --border:      rgba(168, 153, 104, 0.15);
    --border-strong: rgba(168, 153, 104, 0.3);
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  html, body {
    font-family: 'Rubik', sans-serif;
    background: var(--bg);
    color: var(--text);
    min-height: 100vh;
    min-height: 100dvh;
    font-weight: 400;
    line-height: 1.5;
    -webkit-font-smoothing: antialiased;
  }

  body {
    background-image:
      radial-gradient(circle at 15% 10%, rgba(45, 59, 40, 0.4) 0%, transparent 50%),
      radial-gradient(circle at 85% 90%, rgba(20, 23, 18, 0.8) 0%, transparent 50%),
      repeating-linear-gradient(45deg, transparent, transparent 2px, rgba(168,153,104,0.015) 2px, rgba(168,153,104,0.015) 4px);
  }

  .container {
    max-width: 1440px;
    margin: 0 auto;
    padding: 0 2rem;
  }

  /* ── Top ribbon ── */
  .ribbon {
    background: var(--bg-deep);
    border-bottom: 1px solid var(--border);
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.15em;
    color: var(--text-faint);
    padding: 0.5rem 0;
    text-transform: uppercase;
  }

  .ribbon .container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 1rem;
    flex-wrap: wrap;
  }

  .ribbon-left { display: flex; gap: 2rem; flex-wrap: wrap; }
  .ribbon-right { display: flex; gap: 1.5rem; align-items: center; flex-wrap: wrap; }

  .ribbon-dot {
    width: 6px; height: 6px; border-radius: 50%;
    background: var(--text-faint);
    display: inline-block;
    margin-right: 0.5rem;
  }
  .ribbon-dot.online { background: var(--safe); box-shadow: 0 0 8px var(--safe); animation: pulse 2s infinite; }
  .ribbon-dot.offline { background: var(--danger); }

  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:0.3} }

  /* ── Header ── */
  header {
    padding: 1.5rem 0 1.2rem;
    border-bottom: 2px solid var(--border-strong);
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 2rem;
    position: relative;
    flex-wrap: wrap;
  }

  header::after {
    content: '';
    position: absolute;
    bottom: -2px;
    left: 0;
    width: 80px;
    height: 2px;
    background: var(--amber);
  }

  .brand {
    display: flex;
    align-items: center;
    gap: 1rem;
  }

  .brand-insignia {
    width: 56px; height: 56px;
    position: relative;
    border: 2px solid var(--amber);
    background: var(--bg-deep);
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Oswald', sans-serif;
    font-size: 1.4rem;
    font-weight: 700;
    color: var(--amber);
    letter-spacing: 0.05em;
    transform: rotate(45deg);
    flex-shrink: 0;
  }

  .brand-insignia span { transform: rotate(-45deg); }

  .brand-text h1 {
    font-family: 'Oswald', sans-serif;
    font-size: 2rem;
    font-weight: 700;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    color: var(--bone);
    line-height: 1;
  }

  .brand-subtitle {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.68rem;
    letter-spacing: 0.2em;
    color: var(--khaki);
    text-transform: uppercase;
    margin-top: 0.3rem;
  }

  .header-stats {
    display: flex;
    gap: 0;
    border: 1px solid var(--border-strong);
    background: var(--bg-panel);
  }

  .hstat {
    padding: 0.8rem 1.4rem;
    text-align: center;
    border-right: 1px solid var(--border);
    min-width: 110px;
  }

  .hstat:last-child { border-right: none; }

  .hstat-val {
    font-family: 'Oswald', sans-serif;
    font-size: 1.6rem;
    font-weight: 600;
    color: var(--amber);
    line-height: 1;
  }

  .hstat-lbl {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.62rem;
    letter-spacing: 0.15em;
    color: var(--text-dim);
    text-transform: uppercase;
    margin-top: 0.3rem;
  }

  /* ── Main layout ── */
  .main {
    padding: 2rem 0 4rem;
    display: grid;
    grid-template-columns: 1.3fr 1fr;
    gap: 2rem;
  }

  /* ── Panel headers ── */
  .panel-header {
    display: flex;
    align-items: center;
    gap: 0.8rem;
    margin-bottom: 1rem;
    padding-bottom: 0.7rem;
    border-bottom: 1px solid var(--border);
  }

  .panel-header-mark { width: 18px; height: 2px; background: var(--amber); }

  .panel-header h2 {
    font-family: 'Oswald', sans-serif;
    font-size: 0.95rem;
    font-weight: 600;
    letter-spacing: 0.15em;
    color: var(--khaki);
    text-transform: uppercase;
    flex: 1;
  }

  .panel-header-meta {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.08em;
    color: var(--text-faint);
    text-transform: uppercase;
  }

  .download-btn {
    background: transparent;
    border: 1px solid var(--border-strong);
    color: var(--khaki);
    font-family: 'Oswald', sans-serif;
    font-size: 0.7rem;
    letter-spacing: 0.15em;
    padding: 0.35rem 0.75rem;
    cursor: pointer;
    text-transform: uppercase;
    transition: all 0.15s;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
  }

  .download-btn:hover {
    background: var(--amber);
    color: var(--bg-deep);
    border-color: var(--amber);
  }

  /* ── Viewfinder ── */
  .viewfinder {
    background: #000;
    position: relative;
    aspect-ratio: 4 / 3;
    overflow: hidden;
    border: 1px solid var(--border-strong);
  }

  .viewfinder img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
  }

  .reticle { position: absolute; inset: 0; pointer-events: none; }
  .reticle-line { position: absolute; background: rgba(212, 152, 64, 0.25); }
  .reticle-line.h { left: 10%; right: 10%; top: 50%; height: 1px; }
  .reticle-line.v { top: 10%; bottom: 10%; left: 50%; width: 1px; }

  .reticle-center {
    position: absolute;
    top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    width: 20px; height: 20px;
    border: 1px solid rgba(212, 152, 64, 0.4);
    border-radius: 50%;
  }

  .reticle-center::before,
  .reticle-center::after {
    content: '';
    position: absolute;
    background: rgba(212, 152, 64, 0.4);
  }

  .reticle-center::before { left: 50%; top: -4px; bottom: -4px; width: 1px; transform: translateX(-50%); }
  .reticle-center::after  { top: 50%; left: -4px; right: -4px; height: 1px; transform: translateY(-50%); }

  .corner {
    position: absolute;
    width: 24px; height: 24px;
    border: 2px solid var(--amber);
  }
  .corner.tl { top: 10px; left: 10px; border-right: none; border-bottom: none; }
  .corner.tr { top: 10px; right: 10px; border-left: none; border-bottom: none; }
  .corner.bl { bottom: 10px; left: 10px; border-right: none; border-top: none; }
  .corner.br { bottom: 10px; right: 10px; border-left: none; border-top: none; }

  .cam-header {
    position: absolute;
    top: 0; left: 0; right: 0;
    padding: 0.8rem 1rem;
    background: linear-gradient(to bottom, rgba(0,0,0,0.7), transparent);
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    color: var(--bone);
    letter-spacing: 0.08em;
  }

  .cam-id { display: flex; align-items: center; gap: 0.5rem; }

  .rec-dot {
    width: 8px; height: 8px; border-radius: 50%;
    background: var(--danger);
    animation: rec-blink 1.5s infinite;
  }

  @keyframes rec-blink { 0%,40%{opacity:1} 60%,100%{opacity:0.2} }

  .cam-footer {
    position: absolute;
    bottom: 0; left: 0; right: 0;
    padding: 0.8rem 1rem 1rem;
    background: linear-gradient(to top, rgba(0,0,0,0.8), transparent);
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.68rem;
    color: var(--bone);
    letter-spacing: 0.06em;
  }

  .cam-footer-row {
    display: flex;
    justify-content: space-between;
    margin-bottom: 0.5rem;
  }

  .motion-meter {
    height: 4px;
    background: rgba(255, 255, 255, 0.15);
    border-radius: 1px;
    overflow: hidden;
  }

  .motion-meter-fill {
    height: 100%;
    background: linear-gradient(90deg, var(--moss), var(--amber), var(--danger));
    width: 0%;
    transition: width 0.3s ease;
  }

  .cam-controls {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-top: 0.8rem;
    padding: 0.8rem 1rem;
    background: var(--bg-panel);
    border: 1px solid var(--border);
    gap: 0.5rem;
    flex-wrap: wrap;
  }

  .view-toggle {
    display: flex;
    background: var(--bg-deep);
    border: 1px solid var(--border);
  }

  .view-toggle button {
    background: transparent;
    border: none;
    padding: 0.5rem 1rem;
    font-family: 'Oswald', sans-serif;
    font-size: 0.75rem;
    letter-spacing: 0.15em;
    color: var(--text-dim);
    cursor: pointer;
    text-transform: uppercase;
    font-weight: 500;
    transition: all 0.15s;
  }

  .view-toggle button:not(:last-child) { border-right: 1px solid var(--border); }

  .view-toggle button.active {
    background: var(--amber);
    color: var(--bg-deep);
  }

  .view-toggle button:hover:not(.active) { color: var(--bone); }

  .timestamp-display {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    color: var(--khaki);
    letter-spacing: 0.08em;
  }

  /* ── Sidebar ── */
  .sidebar {
    display: flex;
    flex-direction: column;
    gap: 1.8rem;
  }

  /* ── Target panel ── */
  .target-panel {
    background: var(--bg-panel);
    border: 1px solid var(--border-strong);
    position: relative;
  }

  .target-panel::before {
    content: '';
    position: absolute;
    top: -1px; left: -1px; right: -1px;
    height: 3px;
    background: linear-gradient(90deg, var(--amber) 0%, var(--amber) 40%, transparent 40%);
  }

  .no-target {
    text-align: center;
    padding: 2rem 1rem;
    color: var(--text-dim);
    font-family: 'Rubik', sans-serif;
    font-size: 0.9rem;
  }

  .no-target::before {
    content: 'NO TARGET ACQUIRED';
    display: block;
    font-family: 'Oswald', sans-serif;
    font-size: 0.8rem;
    letter-spacing: 0.2em;
    color: var(--text-faint);
    margin-bottom: 0.5rem;
  }

  .target-entry {
    padding: 1.1rem 1.2rem;
    border-bottom: 1px solid var(--border);
    display: flex;
    align-items: center;
    gap: 1rem;
    flex-wrap: wrap;
  }

  .target-entry:last-child { border-bottom: none; }

  .target-plate {
    width: 52px; height: 52px;
    background: var(--bg-deep);
    border: 1px solid var(--border-strong);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.7rem;
    position: relative;
    flex-shrink: 0;
  }

  .target-plate::after {
    content: '';
    position: absolute;
    inset: -4px;
    border: 1px dashed var(--khaki);
    opacity: 0.3;
  }

  .target-body { flex: 1; min-width: 120px; }

  .target-species {
    font-family: 'Oswald', sans-serif;
    font-size: 1.2rem;
    font-weight: 600;
    color: var(--bone);
    text-transform: uppercase;
    letter-spacing: 0.08em;
    line-height: 1;
  }

  .target-sci {
    font-family: 'Rubik', sans-serif;
    font-style: italic;
    font-size: 0.75rem;
    color: var(--text-dim);
    margin-top: 0.3rem;
  }

  .target-meta {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    margin-top: 0.6rem;
  }

  .confidence-track {
    width: 80px;
    height: 4px;
    background: var(--bg-deep);
    border: 1px solid var(--border);
    overflow: hidden;
  }

  .confidence-fill {
    height: 100%;
    background: linear-gradient(90deg, var(--moss), var(--amber));
    transition: width 0.5s ease;
  }

  .confidence-pct {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    color: var(--amber);
    letter-spacing: 0.05em;
    font-weight: 500;
  }

  .hunt-status {
    text-align: center;
    padding: 0.4rem 0.7rem;
    border: 1px solid;
    font-family: 'Oswald', sans-serif;
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    white-space: nowrap;
  }

  .hunt-status.legal {
    color: var(--safe);
    border-color: var(--safe);
    background: rgba(107, 148, 71, 0.08);
  }

  .hunt-status.illegal {
    color: var(--danger);
    border-color: var(--danger);
    background: rgba(194, 61, 46, 0.08);
  }

  .hunt-status.illegal::before { content: '⚠ '; }

  /* ── Logbook ── */
  .logbook {
    background: var(--bg-panel);
    border: 1px solid var(--border-strong);
  }

  .log-entry {
    display: grid;
    grid-template-columns: 70px 1fr auto;
    gap: 0.8rem;
    padding: 0.7rem 1.2rem;
    border-bottom: 1px solid var(--border);
    align-items: center;
    font-size: 0.85rem;
  }

  .log-entry:last-child { border-bottom: none; }
  .log-entry:hover { background: rgba(168, 153, 104, 0.03); }

  .log-time {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    color: var(--khaki);
    letter-spacing: 0.04em;
    font-weight: 500;
  }

  .log-species {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-family: 'Oswald', sans-serif;
    color: var(--bone);
    text-transform: uppercase;
    letter-spacing: 0.08em;
    font-size: 0.85rem;
    font-weight: 500;
    min-width: 0;
  }

  .log-species .emoji { font-size: 1.1rem; line-height: 1; flex-shrink: 0; }

  .log-indicator {
    width: 6px; height: 6px; border-radius: 50%;
    flex-shrink: 0;
  }

  .log-indicator.legal { background: var(--safe); }
  .log-indicator.illegal { background: var(--danger); }

  .log-empty {
    text-align: center;
    padding: 2rem;
    color: var(--text-faint);
    font-family: 'Rubik', sans-serif;
    font-size: 0.85rem;
  }

  /* ── Big total counter ── */
  .total-counter {
    background: var(--bg-panel);
    border: 1px solid var(--border-strong);
    padding: 2rem 1.5rem;
    text-align: center;
    position: relative;
  }

  .total-counter::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: var(--amber);
    opacity: 0.5;
  }

  .total-counter-num {
    font-family: 'Oswald', sans-serif;
    font-size: 4.5rem;
    font-weight: 700;
    color: var(--amber);
    line-height: 1;
    letter-spacing: -0.02em;
  }

  .total-counter-lbl {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.25em;
    color: var(--text-dim);
    text-transform: uppercase;
    margin-top: 0.8rem;
  }

  .total-counter-sublbl {
    font-family: 'Rubik', sans-serif;
    font-size: 0.75rem;
    color: var(--text-faint);
    margin-top: 0.4rem;
    font-style: italic;
  }

  /* ── Footer ── */
  .footer {
    margin-top: 3rem;
    padding: 1.2rem 0;
    border-top: 1px solid var(--border);
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.68rem;
    color: var(--text-faint);
    letter-spacing: 0.08em;
    text-transform: uppercase;
    gap: 1rem;
    flex-wrap: wrap;
  }

  .api-config { display: flex; align-items: center; gap: 0.5rem; }

  .api-config input {
    background: transparent;
    border: none;
    border-bottom: 1px dashed var(--border-strong);
    padding: 0.2rem 0.4rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    color: var(--amber);
    outline: none;
    width: 200px;
  }

  .api-config input:focus { border-bottom-color: var(--amber); }

  /* ═══════════════════════════════════════════════════════════════
     RESPONSIVE — TABLET
     ═══════════════════════════════════════════════════════════════ */
  @media (max-width: 1024px) {
    .main {
      grid-template-columns: 1fr;
      gap: 1.5rem;
    }

    .header-stats {
      order: 3;
      flex: 1 1 100%;
    }

    .hstat { flex: 1; min-width: auto; }

    .total-counter-num { font-size: 4rem; }
  }

  /* ═══════════════════════════════════════════════════════════════
     RESPONSIVE — PHONE
     ═══════════════════════════════════════════════════════════════ */
  @media (max-width: 640px) {
    .container { padding: 0 1rem; }

    .ribbon { font-size: 0.6rem; padding: 0.4rem 0; }
    .ribbon .container { gap: 0.5rem; }
    .ribbon-left { gap: 1rem; }
    .ribbon-right { gap: 0.8rem; }

    header {
      padding: 1.2rem 0 1rem;
      flex-direction: column;
      align-items: stretch;
      gap: 1rem;
    }

    .brand-insignia {
      width: 44px; height: 44px;
      font-size: 1.1rem;
    }

    .brand-text h1 { font-size: 1.5rem; }
    .brand-subtitle { font-size: 0.6rem; }

    .header-stats {
      width: 100%;
    }

    .hstat {
      padding: 0.7rem 0.5rem;
      min-width: 0;
    }

    .hstat-val { font-size: 1.3rem; }
    .hstat-lbl { font-size: 0.55rem; letter-spacing: 0.1em; }

    .main { padding: 1.5rem 0 3rem; gap: 1.5rem; }

    .panel-header h2 { font-size: 0.85rem; letter-spacing: 0.12em; }

    .viewfinder {
      aspect-ratio: 1 / 1;
    }

    .corner { width: 18px; height: 18px; }

    .cam-header { font-size: 0.62rem; padding: 0.6rem 0.8rem; }
    .cam-footer { font-size: 0.6rem; padding: 0.6rem 0.8rem 0.8rem; }

    .cam-controls {
      padding: 0.6rem 0.8rem;
      flex-direction: column;
      align-items: stretch;
      gap: 0.5rem;
    }

    .view-toggle { justify-content: center; }
    .view-toggle button {
      flex: 1;
      padding: 0.5rem 0.5rem;
      font-size: 0.68rem;
    }

    .timestamp-display {
      text-align: center;
      font-size: 0.65rem;
    }

    .target-entry {
      padding: 1rem;
      gap: 0.8rem;
    }

    .target-plate {
      width: 44px; height: 44px;
      font-size: 1.4rem;
    }

    .target-species { font-size: 1rem; }
    .target-sci { font-size: 0.7rem; }

    .hunt-status {
      font-size: 0.6rem;
      padding: 0.3rem 0.5rem;
      letter-spacing: 0.12em;
    }

    .log-entry {
      grid-template-columns: 60px 1fr auto;
      gap: 0.5rem;
      padding: 0.6rem 0.8rem;
      font-size: 0.8rem;
    }

    .log-time { font-size: 0.65rem; }
    .log-species { font-size: 0.75rem; letter-spacing: 0.05em; }

    .total-counter { padding: 1.5rem 1rem; }
    .total-counter-num { font-size: 3.5rem; }
    .total-counter-lbl { font-size: 0.62rem; letter-spacing: 0.18em; }

    .footer {
      flex-direction: column;
      align-items: stretch;
      text-align: center;
      font-size: 0.6rem;
    }

    .api-config { justify-content: center; flex-wrap: wrap; }
    .api-config input { width: 100%; max-width: 240px; }
  }

  /* Touch-friendly — larger hit areas on touch devices */
  @media (hover: none) and (pointer: coarse) {
    .view-toggle button { padding: 0.7rem 1rem; }
    .download-btn { padding: 0.5rem 0.9rem; }
  }

  ::selection { background: var(--amber); color: var(--bg-deep); }
  ::-webkit-scrollbar { width: 6px; }
  ::-webkit-scrollbar-track { background: var(--bg-deep); }
  ::-webkit-scrollbar-thumb { background: var(--forest); }
</style>
</head>
<body>

<!-- Top ribbon -->
<div class="ribbon">
  <div class="container">
    <div class="ribbon-left">
      <span><span class="ribbon-dot" id="ribbonDot"></span><span id="ribbonStatus">CONNECTING</span></span>
      <span>MOTION-TRIGGERED</span>
    </div>
    <div class="ribbon-right">
      <span>UNIT · WT-PI-01</span>
      <span id="ribbonTime">—</span>
    </div>
  </div>
</div>

<div class="container">

  <!-- Header -->
  <header>
    <div class="brand">
      <div class="brand-insignia"><span>WT</span></div>
      <div class="brand-text">
        <h1>WildTrack</h1>
        <div class="brand-subtitle">Trail Camera Intelligence</div>
      </div>
    </div>

    <div class="header-stats">
      <div class="hstat">
        <div class="hstat-val" id="hDetections">0</div>
        <div class="hstat-lbl">Sightings</div>
      </div>
      <div class="hstat">
        <div class="hstat-val" id="hIllegal" style="color: var(--danger);">0</div>
        <div class="hstat-lbl">Prohibited</div>
      </div>
    </div>
  </header>

  <!-- Main -->
  <div class="main">

    <!-- Viewfinder -->
    <section>
      <div class="panel-header">
        <div class="panel-header-mark"></div>
        <h2>Live Feed · Pi Cam V3</h2>
        <div class="panel-header-meta" id="feedInfo">STANDBY</div>
      </div>

      <div class="viewfinder">
        <img id="cameraImg" src="" alt="Feed">
        <div class="reticle">
          <div class="reticle-line h"></div>
          <div class="reticle-line v"></div>
          <div class="reticle-center"></div>
        </div>
        <div class="corner tl"></div>
        <div class="corner tr"></div>
        <div class="corner bl"></div>
        <div class="corner br"></div>

        <div class="cam-header">
          <div class="cam-id">
            <span class="rec-dot"></span>
            REC · CH-01
          </div>
          <div id="timeTag">—</div>
        </div>

        <div class="cam-footer">
          <div class="cam-footer-row">
            <span id="motionStateTxt">MONITORING</span>
            <span id="motionPctTxt">0.0% MOTION</span>
          </div>
          <div class="motion-meter">
            <div class="motion-meter-fill" id="motionBar"></div>
          </div>
        </div>
      </div>

      <div class="cam-controls">
        <div class="view-toggle">
          <button class="active" id="btnAnnotated" onclick="setMode('annotated')">Tagged</button>
          <button id="btnRaw" onclick="setMode('raw')">Raw</button>
        </div>
        <div class="timestamp-display" id="latencyInfo">— MS · WAITING</div>
      </div>
    </section>

    <!-- Sidebar -->
    <section class="sidebar">

      <!-- Total counter -->
      <div>
        <div class="panel-header">
          <div class="panel-header-mark"></div>
          <h2>Total Wildlife Detected</h2>
          <div class="panel-header-meta">SESSION</div>
        </div>
        <div class="total-counter">
          <div class="total-counter-num" id="totalCount">0</div>
          <div class="total-counter-lbl">Animals Since Start</div>
          <div class="total-counter-sublbl" id="sessionStart">Session: —</div>
        </div>
      </div>

      <!-- Target acquisition -->
      <div>
        <div class="panel-header">
          <div class="panel-header-mark"></div>
          <h2>Target Acquisition</h2>
          <div class="panel-header-meta">LIVE</div>
        </div>
        <div class="target-panel" id="targetPanel">
          <div class="no-target">Waiting for motion trigger</div>
        </div>
      </div>

      <!-- Log book -->
      <div>
        <div class="panel-header">
          <div class="panel-header-mark"></div>
          <h2>Hunt Log</h2>
          <a class="download-btn" id="downloadBtn" href="#" onclick="downloadLog(event)">
            ↓ LOG FILE
          </a>
        </div>
        <div class="logbook" id="logbook">
          <div class="log-empty">No sightings logged</div>
        </div>
      </div>

    </section>

  </div>

  <!-- Footer -->
  <div class="footer">
    <div>YOLOv8N · FOREST LENS V2 · MAP 0.948</div>
    <div class="api-config">
      <span>ENDPOINT:</span>
      <input id="apiUrl" value="http://192.168.68.116:8000" onchange="updateApiUrl()">
    </div>
  </div>

</div>

<script>
  const SPECIES_ICONS = {
    deer:'🦌', boar:'🐗', rabbit:'🐇', jackal:'🐺', pheasant:'🦃'
  };

  const SPECIES_SCIENTIFIC = {
    deer:     'Cervidae',
    boar:     'Sus scrofa',
    rabbit:   'Lepus europaeus',
    jackal:   'Canis aureus',
    pheasant: 'Phasianus colchicus'
  };

  let apiBase       = 'http://192.168.68.116:8000';
  let frameMode     = 'annotated';
  const sessionStartedAt = new Date();

  document.getElementById('sessionStart').textContent =
    'Session started: ' + sessionStartedAt.toLocaleTimeString();

  function updateApiUrl() {
    apiBase = document.getElementById('apiUrl').value.replace(/\/$/, '');
  }

  function setMode(mode) {
    frameMode = mode;
    document.getElementById('btnAnnotated').className = (mode === 'annotated') ? 'active' : '';
    document.getElementById('btnRaw').className       = (mode === 'raw')        ? 'active' : '';
  }

  function refreshFrame() {
    const img = document.getElementById('cameraImg');
    const url = `${apiBase}/frame/${frameMode}?t=${Date.now()}`;
    const tmp = new Image();
    tmp.onload = () => { img.src = tmp.src; };
    tmp.src = url;
  }

  function updateRibbonTime() {
    const now = new Date();
    const txt = now.toLocaleString('en-US', {
      month: 'short', day: '2-digit',
      hour: '2-digit', minute: '2-digit', second: '2-digit', hour12: false
    }).toUpperCase();
    document.getElementById('ribbonTime').textContent = txt;
  }

  // Download detection log
  function downloadLog(e) {
    e.preventDefault();
    window.open(`${apiBase}/log`, '_blank');
  }

  async function pollLatest() {
    try {
      const r = await fetch(`${apiBase}/latest`);
      if (!r.ok) throw new Error();
      const data = await r.json();

      if (data.status === 'waiting') return;

      document.getElementById('timeTag').textContent    = data.timestamp?.slice(11,19) || '—';
      document.getElementById('latencyInfo').textContent = `${data.latency_ms || '—'} MS · LAST SCAN`;
      document.getElementById('feedInfo').textContent    = data.animal_present ? 'TARGET ACQUIRED' : 'SCANNING';

      renderTarget(data.detections || []);

    } catch(e) { /* silent */ }
  }

  async function pollHealth() {
    const dot = document.getElementById('ribbonDot');
    const txt = document.getElementById('ribbonStatus');
    try {
      const r = await fetch(`${apiBase}/health`, {signal: AbortSignal.timeout(3000)});
      const data = await r.json();
      dot.className = 'ribbon-dot online';
      txt.textContent = 'STATION ONLINE';

      // Use total_detections from API (tracked since detect.py start)
      const total = data.total_detections || 0;
      document.getElementById('totalCount').textContent = total;
      document.getElementById('hDetections').textContent = total;

      const pct = data.motion_pct || 0;
      document.getElementById('motionBar').style.width = Math.min(pct * 4, 100) + '%';
      document.getElementById('motionPctTxt').textContent = pct.toFixed(1) + '% MOTION';

      const stateMap = {
        idle:             'SCANNING',
        motion_detected:  'MOVEMENT DETECTED',
        cooldown:         'COOLDOWN',
        detected:         'TARGET ACQUIRED'
      };
      document.getElementById('motionStateTxt').textContent = stateMap[data.motion_state] || 'SCANNING';

    } catch {
      dot.className = 'ribbon-dot offline';
      txt.textContent = 'STATION OFFLINE';
    }
  }

  async function pollHistory() {
    try {
      const r = await fetch(`${apiBase}/history?limit=15`);
      const data = await r.json();
      renderLogbook(data.results || []);

      // Count illegal from recent history
      const illegal = (data.results || []).reduce((acc, r) => {
        if (!r.animal_present) return acc;
        return acc + r.detections.filter(d => d.legal === 'illegal').length;
      }, 0);
      document.getElementById('hIllegal').textContent = illegal;

    } catch(e) { /* silent */ }
  }

  function renderTarget(detections) {
    const el = document.getElementById('targetPanel');
    if (!detections.length) {
      el.innerHTML = '<div class="no-target">Waiting for motion trigger</div>';
      return;
    }
    el.innerHTML = detections.map(d => {
      const icon     = SPECIES_ICONS[d.species] || '❓';
      const sci      = SPECIES_SCIENTIFIC[d.species] || '';
      const confPct  = Math.round(d.confidence * 100);
      const legalCls = d.legal === 'legal' ? 'legal' : 'illegal';
      const legalTxt = d.legal === 'legal' ? 'Permitted' : 'Prohibited';
      return `
        <div class="target-entry">
          <div class="target-plate">${icon}</div>
          <div class="target-body">
            <div class="target-species">${d.species}</div>
            <div class="target-sci">${sci}</div>
            <div class="target-meta">
              <div class="confidence-track">
                <div class="confidence-fill" style="width:${confPct}%"></div>
              </div>
              <span class="confidence-pct">${confPct}%</span>
            </div>
          </div>
          <div class="hunt-status ${legalCls}">${legalTxt}</div>
        </div>`;
    }).join('');
  }

  function renderLogbook(results) {
    const el = document.getElementById('logbook');
    const withAnimals = results.filter(r => r.animal_present).reverse();
    if (!withAnimals.length) {
      el.innerHTML = '<div class="log-empty">No sightings logged</div>';
      return;
    }
    el.innerHTML = withAnimals.map(r => {
      const first = r.detections[0];
      const icon  = SPECIES_ICONS[first.species] || '❓';
      const indicatorCls = first.legal === 'legal' ? 'legal' : 'illegal';
      return `
        <div class="log-entry">
          <span class="log-time">${r.timestamp?.slice(11,19) || '—'}</span>
          <span class="log-species">
            <span class="log-indicator ${indicatorCls}"></span>
            <span class="emoji">${icon}</span>
            <span>${first.species}</span>
            ${r.detections.length > 1 ? `<span style="color:var(--text-dim);font-size:0.7rem;font-weight:400;">+${r.detections.length - 1}</span>` : ''}
          </span>
          <span class="confidence-pct">${Math.round(first.confidence * 100)}%</span>
        </div>`;
    }).join('');
  }

  updateRibbonTime();
  pollHealth();
  pollLatest();
  pollHistory();

  setInterval(refreshFrame,     800);
  setInterval(pollLatest,       1500);
  setInterval(pollHealth,       2000);
  setInterval(pollHistory,      3000);
  setInterval(updateRibbonTime, 1000);
</script>
</body>
</html>
