document.getElementById("run-script").addEventListener("click", () => {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      chrome.scripting.executeScript({
            target: { tabId: tabs[0].id },
            files: ["index.js"],
        });
    });
});
  