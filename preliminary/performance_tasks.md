# Overview
This section contains preliminary familiarisation steps with the core libraries of the project. It is also designed to complement (and satisfy) the performance requirements of the preliminary assessment.

## Required performance demonstration

You must demonstrate your ability at:

- Determining an organisation’s technology, development tools, and UI platform
- Enabling interprocess communication in Python while using third-party libraries and referencing third-party documentation


## Instructions

1. Complete the knowledge section (Word document) available via Blackboard
2. Fork this repository
3. Clone the repository to your local computer
4. Install `uv` and check that it is running with `uv --version`
5. Obtain a video that can be used to test the functionality and place in the `resources/` folder - your instructor will provide you with one
6. Follow the steps in the remainder of the guide insuring your commit to git whenever prompted
7. Submit a `zip` of this repository along with the `.git` folder. **Do not include your `venv/`**. Ensure your submission includes the assessment Word document with all of the questions in it attempted.


## Steps
Complete the steps below and fill in the `> block` sections
> If you see a section like this, fill it in!


### Installing and running OpenCV

1. Examine the `pyproject.toml` what dependencies does it currently identify?
> ANSWER: The dependencies list is empty. This is how it shows in the version control: "dependencies = []"
> 
2. Create a `.venv` in this folder using `uv venv`
3. Activate the `venv` as instructed by `uv`
4. In order to complete the project, we need to install OpenCV. Fill in the following:
  - What role does OpenCV have in this project?
  > ANSWER: OpenCV is used to work with video and image data. In this project, it can open the video file, 
  read video information, and extract image frames from the video. These frames can later be used by OCR
  to read text from the image.
  - What is the `uv pip` command to install OpenCV?
  > ANSWER: uv pip install opencv-python
  - What is the URL of this library's git repo?
  > ANSWER: https://github.com/opencv/opencv-python
5. Add OpenCV to your project using the `uv add` command:
  > ANSWER: uv add opencv-python

6. Have the dependencies in the `pyproject.toml` changed? If so, how?
  > ANSWER: Yes. Before adding OpenCV, the dependencies list was empty.
  >  After running uv add opencv-python, OpenCV was added to the dependencies list:
  >   "opencv-python>=4.13.0.92"
> 
7. Why did we use `uv add` over `uv pip`?
  > ANSWER: We used uv add because it installs the package and saves it in pyproject.toml. This makes OpenCV
  > part of the project dependencies. uv pip install installs the package into the virtual environment,
  > but uv add is better for keeping the project files updated.
8. The `numpy` library is required for OpenCV. Should you add an explicit requirement for it? Why/Why not? 
  > ANSWER:: No, I do not need to add NumPy manually because OpenCV installs NumPy as a required dependency.
  > In my terminal output, NumPy was installed automatically with OpenCV. I would only add NumPy
  > explicitly if my own code directly used NumPy and needed a specific version. 
9. Commit the changes so far to git. Use the message `chore: add OpenCV dependency`
10. Go to `preliminary/library_basics.py` and complete the required functionality.
11. Commit your changes with `feat: save video frames`


### Installing and running Tesseract

[Tesseract OCR](https://github.com/tesseract-ocr/tesseract) provides optical character recognition (OCR) functionality needed for the project.

Tesseract consists of both an OCR Engine and a command line program. It is predominantly written in C++.

1. Examine the [Readme](https://github.com/tesseract-ocr/tesseract?tab=readme-ov-file) and find a list of Python wrappers.

2. What is the URL that lists Python wrappers for Tesseract?
  > ANSWER: https://tesseract-ocr.github.io/tessdoc/AddOns.html

3. Select a Python wrapper. What wrapper did you choose and why? Ensure you address each element below in your answer
> ANSWER: I chose pytesseract because it is a Python wrapper for Google Tesseract OCR. It suits this project
> because it can read text from video frames and return it as normal text.
> It has recent activity on GitHub, but it also needs the Tesseract OCR engine installed
> separately. OpenCV can extract the image frame, and pytesseract can read the text from it.
> 

4. Use UV to add the dependency to your project and your `pyproject.toml`

5. If your library has additional requirements (e.g. installing tesseract binaries), note it in your README.md

6. Commit the new dependency `chore: add tesseract dependency`

7. Add a new method in `library_basics.py` that returns the text of a given frame/time/image (you decide!)

8. Commit the changes as `feat: OCR an image


### Install and run FastAPI

FastAPI will allow us to enable communication with our OCR service from other processes on the current machine or across a network.

1. Add the requirement for FastAPI using UV. FastAPI has optional requirements so the command is a little different:
`uv add fastapi --extra standard`
2. Commit the new dependency `chore: add FastAPI dependency`
3. Run in development mode using:
`uv run fastapi dev preliminary/simple_api.py`
4. Run the following curl command (may require git bash on Windows):
`curl 127.0.0.1:8000/video`
5. Confirm that a list of videos and URLs is returned by copying the output below:
> ANSWER:
> StatusCode        : 200
StatusDescription : OK
Content           : {"count":1,"videos":[{"id":"demo","path":"..\\resources\\oop.mp4","_links":{"self":"/video/demo","frame_example":"/video/d 
                    emo/frame/1.0"}}]}
RawContent        : HTTP/1.1 200 OK
                    Content-Length: 140
                    Content-Type: application/json
                    Date: Sun, 21 Jun 2026 17:18:47 GMT
                    Server: uvicorn
                    {"count":1,"videos":[{"id":"demo","path":"..\\resources\\oop.mp4","_links"...
Forms             : {}
Headers           : {[Content-Length, 140], [Content-Type, application/json], [Date, Sun, 21 Jun 2026 17:18:47 GMT], [Server, uvicorn]}        
Images            : {}
InputFields       : {}
Links             : {}
ParsedHtml        : mshtml.HTMLDocumentClass
RawContentLength  : 140

6. What are the names of the two processes that just communicated?
>ANSWER:
>The two processes were the curl process and the FastAPI/Uvicorn server process. Curl sent the HTTP request,
>and the FastAPI server received the request and returned the response.
6. Modify the simple_api.py so that it works correctly with your implementation and complete any TODO markers
7. Demonstrate the use of at least two other end points below:
> ANSWER:
>Endpoint 1:
Command used:
"curl 127.0.0.1:8000/video/demo"
Result:
This endpoint returned the metadata for the demo video, including FPS, frame count, and duration
>-------------------------------------------------------------------------------------------
Endpoint 2:
Command used:
"curl 127.0.0.1:8000/video/demo/frame/42/ocr"
Result:
This endpoint returned OCR text from the video frame at 42 seconds.
--------------------------------------------------------------------------------------
Endpoint 3:
Command used:
"curl.exe 127.0.0.1:8000/video/demo/frame/42 --output api_frame.png"
Result:
This endpoint returned an image frame from the video and saved it as "api_frame.png".
>
