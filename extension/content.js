console.log("AI Email Assistant Loaded");

function addAIButton() {
  const composeBox = document.querySelector("div[aria-label='Message Body']");

if (composeBox && !document.getElementById("ai-reply-container")) {
const container = document.createElement("div");
container.id = "ai-reply-container";
container.style.display = "flex";
container.style.gap = "8px";
container.style.marginTop = "10px";
container.style.alignItems = "center";

function makeBtn(label) {
  const b = document.createElement("button");
  b.innerText = label;
  b.style.padding = "6px 12px";
  b.style.backgroundColor = "#4285F4";
  b.style.color = "white";
  b.style.border = "none";
  b.style.borderRadius = "6px";
  b.style.cursor = "pointer";
  return b;
}

const btnProfessional = makeBtn("💼 Professional");
const btnCasual = makeBtn("😊 Casual");
const btnShort = makeBtn("⚡ Short");
const btnDetailed = makeBtn("📝 Detailed");
const btnSummarize = makeBtn("🧾 Summarize");
btnSummarize.style.backgroundColor = "#34A853";

async function generate(tone, clickedBtn) {
  // --- EMAIL EXTRACTION (keep your current working extractor) ---
  const bodies = Array.from(document.querySelectorAll("div.a3s.aiL"));
  const boxRect = composeBox.getBoundingClientRect();
  const candidates = bodies
    .map(el => ({ el, rect: el.getBoundingClientRect() }))
    .filter(x => x.rect.bottom <= boxRect.top);
  candidates.sort((a, b) => b.rect.bottom - a.rect.bottom);
  const emailText = candidates.length ? candidates[0].el.innerText.trim() : "";

  if (!emailText) {
    alert("Could not find the email text above the reply box.");
    return;
  }

  const originalText = clickedBtn.innerText;
  clickedBtn.innerText = "Generating...";

  try {
    const response = await fetch("http://localhost:3001/generate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ emailText, tone })
    });

    const data = await response.json();
    composeBox.innerText = data.reply;
    clickedBtn.innerText = originalText;
  } catch (err) {
    console.error(err);
    clickedBtn.innerText = "Error";
  }
}

btnProfessional.onclick = () => generate("professional", btnProfessional);
btnCasual.onclick = () => generate("casual", btnCasual);
btnShort.onclick = () => generate("short", btnShort);
btnDetailed.onclick = () => generate("detailed", btnDetailed);
btnSummarize.onclick = () => generate("summarize", btnSummarize);

container.appendChild(btnProfessional);
container.appendChild(btnCasual);
container.appendChild(btnShort);
container.appendChild(btnDetailed);
container.appendChild(btnSummarize);

composeBox.parentElement.appendChild(container);
    button.innerText = "✨ AI Reply";
    button.id = "ai-reply-btn";

    button.style.marginTop = "10px";
    button.style.padding = "6px 12px";
    button.style.backgroundColor = "#4285F4";
    button.style.color = "white";
    button.style.border = "none";
    button.style.borderRadius = "6px";
    button.style.cursor = "pointer";

    button.onclick = async () => {

// Small delay so Gmail finishes rendering when Reply is clicked
await new Promise(r => setTimeout(r, 200));

const bodies = Array.from(document.querySelectorAll("div.a3s.aiL"));

const boxRect = composeBox.getBoundingClientRect();

// Keep only bodies that appear ABOVE the compose box
const candidates = bodies
  .map(el => ({ el, rect: el.getBoundingClientRect() }))
  .filter(x => x.rect.bottom <= boxRect.top);

// Pick the closest one (largest bottom)
candidates.sort((a, b) => b.rect.bottom - a.rect.bottom);

const emailText = candidates.length ? candidates[0].el.innerText.trim() : "";

if (!emailText) {
  alert("Could not find the email text for this reply box. Try clicking Reply again.");
  return;
}

      button.innerText = "Generating...";

      try {
        const response = await fetch("http://localhost:3001/generate", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({ emailText })
        });

        const data = await response.json();

        composeBox.innerText = data.reply;
        button.innerText = "✨ AI Reply";
      } catch (err) {
        console.error(err);
        button.innerText = "Error";
      }
    };

    composeBox.parentElement.appendChild(button);
  }
}

setInterval(addAIButton, 2000);
