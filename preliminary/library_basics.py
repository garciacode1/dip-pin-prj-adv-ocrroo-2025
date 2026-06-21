"""A basic introduction to Open CV

Instructions
------------

Implement the functions below based on their docstrings.

Notice some docstrings include references to third-party documentation
Some docstrings **require** you to add references to third-party documentation.

Make sure you read the docstrings C.A.R.E.F.U.L.Y (yes, I took the L to check that you are awake!)
"""

# imports - add all required imports here
from pathlib import Path
import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

VID_PATH = Path("resources/oop.mp4")


class CodingVideo:
    capture: cv2.VideoCapture

    def __init__(self, video: Path | str):
        self.capture = cv2.VideoCapture(str(video))
        if not self.capture.isOpened():
            raise ValueError(f"Cannot open {video}")

        self.fps = self.capture.get(cv2.CAP_PROP_FPS)
        self.frame_count = int(self.capture.get(cv2.CAP_PROP_FRAME_COUNT))
        self.duration = self.frame_count / self.fps

    def __str__(self) -> str:
        """Displays key metadata from the video

        Specifically, the following information is shown:
            FPS - Number of frames per second rounded to two decimal points
            FRAME COUNT - The total number of frames in the video
            DURATION (minutes) - Calculated total duration of the video given FPS and FRAME COUNT

        Reference
        ----------
        https://docs.opencv.org/3.4/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d
        """
        duration_minutes = self.duration / 60

        return (
            f"FPS: {self.fps:.2f}\n"
            f"FRAME COUNT: {self.frame_count}\n"
            f"DURATION (minutes): {duration_minutes:.2f}"
        )

    def get_frame_number_at_time(self, seconds: int) -> int:
        """Given a time in seconds, returns the value of the nearest frame"""
        return int(seconds * self.fps)

    def get_frame_rgb_array(self, frame_number: int) -> np.ndarray:
        """Returns a numpy N-dimensional array (ndarray)

        The array represents the RGB values of each pixel in a given frame

        Note: cv2 defaults to BGR format, so this function converts the color space to RGB

        Reference
        ---------
        https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html

        """
        self.capture.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
        ok, frame = self.capture.read()
        if not ok or frame is None:
            raise ValueError("Invalid frame number")
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return rgb_frame

    def get_image_as_bytes(self, seconds: int) -> bytes:
        self.capture.set(cv2.CAP_PROP_POS_FRAMES, self.get_frame_number_at_time(seconds))
        ok, frame = self.capture.read()
        if not ok or frame is None:
            raise ValueError("Invalid frame in target location")
        ok, buf = cv2.imencode(".png", frame)
        if not ok:
            raise ValueError("Failed to encode frame")
        return buf.tobytes()

    def save_as_image(self, seconds: int, output_path: Path | str = 'output.png') -> None:
        """Saves the given frame as a png image.
        Reference ---------
        https://docs.opencv.org/4.x/d4/da8/group__imgcodecs.html
        """
        frame_number = self.get_frame_number_at_time(seconds)
        self.capture.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
        ok, frame = self.capture.read()
        if not ok or frame is None:
            raise ValueError("Invalid frame in target location")

        cv2.imwrite(str(output_path), frame)

    def get_text_at_time(self, seconds: int) -> str:
        """Returns OCR text from a video frame at a given time.

        This method gets a frame from the video, converts it to RGB,
        and uses pytesseract to read text from the image.

        Reference
        ---------
        https://github.com/madmaze/pytesseract
        """
        frame_number = self.get_frame_number_at_time(seconds)

        rgb_frame = self.get_frame_rgb_array(frame_number)

        text = pytesseract.image_to_string(rgb_frame)

        return text.strip()


def test():
    """Try out your class here"""
    oop = CodingVideo("resources/oop.mp4")
    print(oop)
    oop.save_as_image(42)

    text = oop.get_text_at_time(42)
    print("OCR TEXT:")
    print(text)


if __name__ == '__main__':
    test()
