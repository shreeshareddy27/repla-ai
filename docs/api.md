# API Reference

## Base URL

Local server: http://localhost:3000

---

## POST /generate

Generates an AI draft reply from provided email content.

---

### Request Body

{
  "email_content": "Full email thread text here..."
}

### Response

{
  "reply": "Generated draft reply text..."
}


Flow
Chrome extension extracts email thread.
Sends POST request to /generate.
Backend formats prompt.
Request forwarded to Ollama runtime.
Generated text returned to extension.

Error Handling
Possible responses:
500 — Ollama not running
400 — Missing email content
503 — Model unavailableSecurity Notes

Server runs locally only.
No authentication required (development mode).
Not exposed to external network by default.



