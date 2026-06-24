const API_BASE_URL = "http://127.0.0.1:8000";

const videoSelect = document.getElementById("videoSelect");
const timeInput = document.getElementById("timeInput");
const message = document.getElementById("message");
const frameImage = document.getElementById("frameImage");
const framePlaceholder = document.getElementById("framePlaceholder");
const ocrResult = document.getElementById("ocrResult");

function getSelectedVideoId() {
    return videoSelect.value;
}

function getTimeValue() {
    return timeInput.value;
}

function validateTime() {
    const time = getTimeValue();
    const maxDuration = 85;

    if (time === "") {
        message.textContent = "Please enter a time in seconds.";
        return false;
    }

    const timeNumber = Number(time);

    if (isNaN(timeNumber)) {
        message.textContent = "Time must be a valid number.";
        return false;
    }

    if (timeNumber < 0) {
        message.textContent = "Time cannot be negative.";
        return false;
    }

    if (timeNumber > maxDuration) {
        message.textContent = "Time must be within the video duration, between 0 and 85 seconds.";
        return false;
    }

    message.textContent = "Input is valid.";
    return true;
}

document.getElementById("previewBtn").addEventListener("click", function () {
    if (!validateTime()) {
        return;
    }

    const videoId = getSelectedVideoId();
    const time = getTimeValue();

    const imageUrl = `${API_BASE_URL}/video/${videoId}/frame/${time}`;

    frameImage.src = imageUrl;
    frameImage.style.display = "block";
    framePlaceholder.style.display = "none";

    message.textContent = "Frame preview loaded.";
});

document.getElementById("ocrBtn").addEventListener("click", async function () {
    if (!validateTime()) {
        return;
    }

    const videoId = getSelectedVideoId();
    const time = getTimeValue();

    const ocrUrl = `${API_BASE_URL}/video/${videoId}/frame/${time}/ocr`;

    message.textContent = "Running OCR...";
    ocrResult.textContent = "Loading OCR result...";

    try {
        const response = await fetch(ocrUrl);

        if (!response.ok) {
            throw new Error("OCR request failed.");
        }

        const data = await response.json();

        ocrResult.textContent = data.text || "No text was detected.";
        message.textContent = "OCR completed.";

    } catch (error) {
        ocrResult.textContent = "OCR failed.";
        message.textContent = "Error: " + error.message;
    }
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