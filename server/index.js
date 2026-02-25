
const express = require("express");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json());

app.get("/", (req, res) => {
  res.json({ ok: true, message: "AI Email Assistant server running" });
});

app.post("/generate", async (req, res) => {
  try {
const { emailText, tone = "professional" } = req.body;
console.log("TONE RECEIVED:", tone);

    if (!emailText) {
      return res.status(400).json({ error: "emailText is required" });
    }

let instruction = "";

switch (tone) {
  case "professional":
    instruction = "Write a professional, concise email reply. No subject line. Reply only.";
    break;
  case "casual":
    instruction = "Write a friendly, casual email reply. No subject line. Reply only.";
    break;
  case "short":
    instruction = "Write a very short email reply (1-2 sentences). No subject line. Reply only.";
    break;
  case "detailed":
    instruction = "Write a detailed email reply with helpful context. No subject line. Reply only.";
    break;
  case "summarize":
    instruction = "Summarize the email thread in 3-6 bullet points. Include key decisions, dates, and action items. Only bullet points.";
    break;
  default:
    instruction = "Write a professional, concise email reply. No subject line. Reply only.";
}

const prompt = `
You are an email assistant.
${instruction}

Email/Thread:
${emailText}
`.trim();


    const ollamaRes = await fetch("http://localhost:11434/api/generate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        model: "llama3.1:latest",
        prompt,
        stream: false
      })
    });

    const data = await ollamaRes.json();
    res.json({ reply: data.response });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Server error", details: String(err) });
  }
});

const PORT = 3001;
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});

