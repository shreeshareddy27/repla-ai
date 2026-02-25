<p align="center">
  <img src="images/logo.png" width="140" alt="Repla.ai logo" />
</p>

<h1 align="center">Repla.ai</h1>

<p align="center">
  Privacy-first AI Gmail assistant powered by a local LLM (Ollama + Llama 3.1)
</p>

<p align="center">
  Applied AI Systems Project — Chrome Extension × Local LLM × Lightweight API Architecture
</p>

---

## 🧠 Overview

Repla.ai is a privacy-first AI email assistant that generates contextual Gmail replies using a locally running Large Language Model (Llama 3.1 via Ollama).

Unlike cloud-based AI assistants, **all inference happens locally**:

Gmail → Chrome Extension → Local Express API → Ollama (Llama 3.1) → Draft injected back into Gmail

This project explores:

- Applied LLM integration in real user workflows  
- Local inference vs cloud trade-offs  
- Lightweight API orchestration  
- Prompt conditioning for controlled generation  
- UX + ML system design  

---

## 🎯 Problem Statement

Modern AI email tools rely on cloud APIs, raising:

- Privacy concerns  
- Data compliance issues  
- API cost constraints  
- Latency variability  

Repla.ai investigates whether a **fully local LLM pipeline** can deliver useful productivity gains while maintaining complete data privacy.

---

