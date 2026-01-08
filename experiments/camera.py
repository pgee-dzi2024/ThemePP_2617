from __future__ import annotations
import cv2
from typing import Optional
from PIL import Image
import io

class Camera:
    def __init__(self, src: int | str = 0, width: int = 640, height: int = 480, fps: int = 20):
        self.cap = cv2.VideoCapture(src)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.cap.set(cv2.CAP_PROP_FPS, fps)

    def read_frame_jpeg(self) -> Optional[bytes]:
        success, frame = self.cap.read()
        if not success:
            return None
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(rgb)
        buf = io.BytesIO()
        pil_img.save(buf, format="JPEG")
        return buf.getvalue()

    def release(self) -> None:
        if hasattr(self, "cap") and self.cap.isOpened():
            self.cap.release()