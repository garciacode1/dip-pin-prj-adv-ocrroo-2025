const message = document.getElementById("message");
const ocrResult = document.getElementById("ocrResult");

document.getElementById("previewBtn").addEventListener("click", function () {
    message.textContent = "Preview button clicked. API connection will be added next.";
});

document.getElementById("ocrBtn").addEventListener("click", function () {
    ocrResult.textContent = "OCR button clicked. OCR API connection will be added next.";
});

document.getElementById("copyBtn").addEventListener("click", function () {
    navigator.clipboard.writeText(ocrResult.textContent);
    message.textContent = "OCR text copied to clipboard.";
});

document.getElementById("darkModeBtn").addEventListener("click", function () {
    document.body.classList.toggle("dark-mode");
});

document.getElementById("textSizeBtn").addEventListener("click", function () {
    document.body.classList.toggle("large-text");
});

document.getElementById("contrastBtn").addEventListener("click", function () {
    document.body.classList.toggle("high-contrast");
});

