# OCR Video Reader

## Project overview

OCR Video Reader is a client/server application designed to help programming students learn from tutorial videos. The app allows the user to play a video, enter a timestamp, preview a selected video frame, and extract readable text from that frame using OCR.

The project uses a Python FastAPI backend with OpenCV and pytesseract. The frontend is built with HTML, CSS, and JavaScript. The frontend communicates with the backend through HTTP API endpoints.

This project supports users who need help reading code or text from programming videos, including users with visual impairment or users who rely more on visible text than audio.

OCR accuracy depends on the quality of the video frame, text size, and image clarity. Some symbols or small text may not be recognised perfectly.
---

## How to run the backend

1. Open the project folder in PowerShell or Git Bash.

2. Create the virtual environment using UV:

```bash
uv venv
````

3. Activate the virtual environment:

```bash
.venv\Scripts\activate
```

4. Install the project dependencies:

```bash
uv sync
```

5. Run the FastAPI backend:

```bash
uv run fastapi dev preliminary/simple_api.py
```

6. Open the backend in the browser:

```text
http://127.0.0.1:8000/
```

Useful backend endpoints:

```text
http://127.0.0.1:8000/video
http://127.0.0.1:8000/video/demo
http://127.0.0.1:8000/video/demo/frame/42
http://127.0.0.1:8000/video/demo/frame/42/ocr
http://127.0.0.1:8000/docs
```

---

## How to open the frontend

The frontend is located in the `frontend` folder.

Open this file in a web browser:

```text
frontend/index.html
```

The backend must be running before using the preview frame or OCR buttons.

Basic workflow:

1. Open `frontend/index.html`.
2. Play the video if needed.
3. Enter a timestamp, such as `42`.
4. Click **Preview Frame**.
5. Click **Run OCR**.
6. Read or copy the OCR result.

---

## Main features

* Video playback in the frontend
* Timestamp input
* Frame preview from a selected video time
* OCR text extraction from a video frame
* Copy OCR result button
* Client-side validation for timestamp input
* Accessibility and personalisation options:

  * High Contrast
  * Large Text
  * Dark Mode
* FastAPI backend API
* OpenCV video frame extraction
* pytesseract OCR processing

---

## Dependencies

The main project dependencies are managed with UV and listed in `pyproject.toml`.

Main dependencies include:

* `fastapi` - used to build the backend API
* `uvicorn` - used to run the FastAPI server
* `opencv-python` - used to open videos and extract frames
* `pytesseract` - used to read text from images
* `numpy` - used by OpenCV for image array handling

To install all dependencies, run:

```bash
uv sync
```

---

## Tesseract OCR requirement

This project uses `pytesseract` for OCR. However, `pytesseract` is only the Python wrapper. The Tesseract OCR engine must also be installed on the computer.

On Windows, install Tesseract OCR and make sure it is available in the system PATH.

If Tesseract is installed but Python cannot find it, the path can be set in the Python code:

```python
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

Without the Tesseract OCR engine installed, the OCR feature will not work.

---

## Project structure

```text
dip-pin-prj-adv-ocrroo-2025/
│
├── design/
│   ├── persona.md
│   ├── user_stories.md
│   ├── wireframes.md
│   └── ai_prompts.md
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
│
├── preliminary/
│   ├── library_basics.py
│   ├── simple_api.py
│   └── performance_tasks.md
│
├── resources/
│   └── oop.mp4
│
├── pyproject.toml
├── uv.lock
└── README.md
```

---

## Notes

The current MVP uses a preloaded video from the `resources` folder. Video upload and external URL support are shown in the design wireframe as possible future improvements, but they are not part of the current MVP build.

```
```
