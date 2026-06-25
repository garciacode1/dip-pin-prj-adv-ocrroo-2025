"""Provides a simple API for your basic OCR client

Drive the API to complete "interprocess communication"

Requirements
"""

from fastapi import FastAPI, HTTPException
from fastapi import Response
from pydantic import BaseModel
from pathlib import Path
from library_basics import CodingVideo
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# We'll create a lightweight "database" for our videos
# You can add uploads later (not required for assessment)
# For now, we will just hardcode are samples
VIDEOS: dict[str, Path] = {
    "demo": Path("resources/oop.mp4")
}


class VideoMetaData(BaseModel):
    fps: float
    frame_count: int
    duration_seconds: float
    _links: dict | None = None


def _open_vid_or_404(vid: str) -> CodingVideo:
    path = VIDEOS.get(vid)
    if not path or not path.is_file():
        raise HTTPException(status_code=404, detail="Video not found")
    try:
        return CodingVideo(path)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Could not open video {e}")


def _meta(video: CodingVideo) -> VideoMetaData:
    return VideoMetaData(
        fps=video.fps,
        frame_count=video.frame_count,
        duration_seconds=video.duration
    )

@app.get("/video")
def list_videos():
    """List all available videos with HATEOAS-style links."""
    return {
        "count": len(VIDEOS),
        "videos": [
            {
                "id": vid,
                "path": str(path),  # Not standard for debug only
                "_links": {
                    "self": f"/video/{vid}",
                    "frame_example": f"/video/{vid}/frame/1.0"
                }
            }
            for vid, path in VIDEOS.items()
        ]
    }

@app.get("/video/{vid}", response_model=VideoMetaData)
def video(vid: str):
    video = _open_vid_or_404(vid)
    try:
        meta = _meta(video)
        meta._links = {
            "self": f"/video/{vid}",
            "frames": f"/video/{vid}/frame/{{seconds}}"
        }
        return meta
    finally:
        video.capture.release()


@app.get("/video/{vid}/frame/{t}", response_class=Response)
def video_frame(vid: str, t: int):
    video_file = _open_vid_or_404(vid)

    try:
        return Response(content=video_file.get_image_as_bytes(t),
                        media_type="image/png")
    finally:
        video_file.capture.release()


@app.get("/video/{vid}/frame/{t}/ocr")
def video_frame_ocr(vid: str, t: int):
    """Return OCR text from a selected video frame."""
    video_file = _open_vid_or_404(vid)

    try:
        text = video_file.get_text_at_time(t)

        return {
            "video_id": vid,
            "time_seconds": t,
            "text": text
        }

    finally:
        video_file.capture.release()

@app.get("/")
def home():
    return {
        "message": "OCR Video Reader API is running",
        "endpoints": {
            "videos": "/video",
            "docs": "/docs"
        }
    }