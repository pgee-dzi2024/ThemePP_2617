from __future__ import annotations
import cv2
from typing import Optional
from PIL import Image
import io
import numpy as np
import time

class Camera:
    def __init__(
        self,
        src: int | str = 0,
        width: int = 640,
        height: int = 480,
        fps: int = 20,
        jpeg_quality: int = 85,
        expose_error_logs: bool = True,
    ):
        """
        Initialize the camera capture.

        Parameters:
        - src: Video source (default 0 for the primary webcam, or a path/URL)
        - width, height: Desired frame size
        - fps: Desired frames per second
        - jpeg_quality: JPEG quality (1-95)
        - expose_error_logs: Whether to print verbose error logs
        """
        self.src = src
        self.cap = cv2.VideoCapture(src)
        self.expose_error_logs = expose_error_logs

        if not self.cap.isOpened():
            raise RuntimeError(f"Failed to open video source {src}")

        # Apply desired properties
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.cap.set(cv2.CAP_PROP_FPS, fps)

        self.width = int(width)
        self.height = int(height)
        self.fps = int(fps)
        self.jpeg_quality = int(jpeg_quality)

        # Small sanity check to ensure properties took effect
        actual_w = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        actual_h = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        if actual_w != self.width or actual_h != self.height:
            if self.expose_error_logs:
                print(f"Warning: Requested size ({self.width}x{self.height}) "
                      f"not supported by device. Got ({actual_w}x{actual_h}).")

        # Time tracking for fps control if needed
        self._last_frame_time = time.time()

    def __enter__(self) -> "Camera":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.release()

    def is_open(self) -> bool:
        """Return whether the underlying capture is opened."""
        return self.cap.isOpened()

    def read_frame_jpeg(self, jpeg_quality: Optional[int] = None) -> Optional[bytes]:
        """
        Read a frame, convert to JPEG, and return bytes.

        Uses BGR->RGB conversion, then saves as JPEG in memory.

        Parameters:
        - jpeg_quality: Optional override for JPEG quality (1-95). If None, uses self.jpeg_quality.

        Returns:
        - JPEG bytes if frame read successfully, else None.
        """
        success, frame = self.cap.read()
        if not success or frame is None:
            if self.expose_error_logs:
                print("Warning: Failed to read frame from camera.")
            return None

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(rgb)

        quality = int(jpeg_quality) if jpeg_quality is not None else self.jpeg_quality
        quality = max(1, min(95, quality))

        buf = io.BytesIO()
        pil_img.save(buf, format="JPEG", quality=quality)
        return buf.getvalue()

    def read_frame_rgb(self) -> Optional[np.ndarray]:
        """
        Read a frame and return as a NumPy RGB array (height, width, 3) with dtype uint8.

        Returns:
        - RGB numpy array if frame read successfully, else None.
        """
        success, frame = self.cap.read()
        if not success or frame is None:
            if self.expose_error_logs:
                print("Warning: Failed to read frame from camera.")
            return None

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return rgb

    def release(self) -> None:
        """Release the underlying video capture."""
        if hasattr(self, "cap") and self.cap is not None:
            if self.cap.isOpened():
                self.cap.release()
                if self.expose_error_logs:
                    print("Camera released.")

    # Optional: friendly short-circuit for quick use
    def grab(self) -> bool:
        """Capture a frame without processing, return True if frame was grabbed."""
        if not self.cap.isOpened():
            if self.expose_error_logs:
                print("Camera is not opened.")
            return False
        return self.cap.grab()