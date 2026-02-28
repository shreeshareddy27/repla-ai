# Repla.ai — Full Tutorial

This guide explains where everything lives, how components connect, and how to run and test the project end-to-end.

---

## 1) High-Level Flow

Gmail Web UI  
→ Chrome Extension (MV3)  
→ Local Express API  
→ Ollama  
→ Llama 3.1  
→ Draft injected back into Gmail  

All inference runs locally. No external API calls.
---

## 2) Repository Structure (Where Everything Lives)

### Chrome Extension
Location: `extension/`  
Purpose: Injects UI into Gmail and sends requests to the backend.

Key files:
- `extension/manifest.json` — MV3 configuration and permissions
- `extension/content.js` — Injects UI + handles button clicks
- `extension/background.js` — Service worker logic (if used)

---

### Backend (Local Express API)
Location: `server/`  
Purpose: Receives email context → calls Ollama → returns generated draft.

Key files:
- `server/index.js` (or `app.js`) — API entry point
- `server/routes/` — API routes (if structured)
- `server/services/` — Ollama integration (if structured)

---

### Evaluation & Benchmarking
Location: `eval/`  
Purpose: Latency testing, cost comparison, privacy surface plotting.

Key files:
- `benchmark_latency.js`
- `plot_latency.py`
- `plot_cost.py`
- `plot_privacy.py`
- `EVAL_DOCUMENTATION.md`
- `EVALUATION_RESULTS_FINAL.md`

---

### Assets
Location: `assets/`  
Contains:
- `repla-logo.png`
- `architecture.png`
- `repla-demo.gif`
---

## 3) Run the Project Locally

### Step 1 — Start Ollama
```bash
ollama serve
ollama pull llama3.1

Step 2 — Start Backend

cd server
npm install
npm start

Step 3 — Load Chrome Extension

Open chrome://extensions
Enable Developer Mode
Click Load unpacked
Select the extension/ folder

Step 4 — Test in Gmail

Open Gmail
Open an email thread
Click a Repla.ai button
Confirm a draft reply is inserted


