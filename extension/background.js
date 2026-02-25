chrome.runtime.onInstalled.addListener(() => {
  console.log("AI Email Assistant installed ✅");
});

chrome.action.onClicked.addListener(async (tab) => {
  try {
    if (!tab.id) return;

    if (!tab.url || !tab.url.includes("mail.google.com")) {
      console.log("Not Gmail, ignoring click.");
      return;
    }

    console.log("Injecting content script...");

    // Always inject fresh
    await chrome.scripting.executeScript({
      target: { tabId: tab.id },
      files: ["content.js"],
    });

    console.log("Sending OPEN_PROMPT message...");

    await chrome.tabs.sendMessage(tab.id, { type: "OPEN_PROMPT" });

  } catch (err) {
    console.error("Background error:", err);
  }
});
