import time
from dataclasses import dataclass
from typing import Generator, Optional

try:
    import cv2
except ImportError:  # pragma: no cover
    cv2 = None

from django.utils import timezone

from .models import CameraSource, MotionEvent


@dataclass
class StreamStatus:
    connected: bool = False
    error: Optional[str] = None
    fps: float = 0.0
    latency_ms: float = 0.0


class CameraStreamService:
    def __init__(self, camera: CameraSource):
        self.camera = camera
        self.capture = None
        self.previous_gray = None
        self.last_motion_at = None

    def open(self) -> StreamStatus:
        if cv2 is None:
            return StreamStatus(connected=False, error="OpenCV не е инсталиран.")

        try:
            if self.camera.source_type == "ip":
                if not self.camera.stream_url:
                    return StreamStatus(connected=False, error="Липсва stream URL.")
                self.capture = cv2.VideoCapture(self.camera.stream_url)
            else:
                self.capture = cv2.VideoCapture(int(self.camera.device_index))

            if not self.capture or not self.capture.isOpened():
                return StreamStatus(connected=False, error="Не може да се отвори видео източникът.")

            return StreamStatus(connected=True)
        except Exception as exc:
            return StreamStatus(connected=False, error=f"Грешка при отваряне на камерата: {exc}")

    def close(self):
        if self.capture is not None:
            self.capture.release()
            self.capture = None

    def read_frame(self):
        if self.capture is None:
            return None

        success, frame = self.capture.read()
        if not success:
            return None
        return frame

    def process_motion(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        motion_detected = False
        annotated_frame = frame.copy()

        if self.previous_gray is None:
            self.previous_gray = gray
            return annotated_frame, motion_detected

        frame_delta = cv2.absdiff(self.previous_gray, gray)
        thresh = cv2.threshold(
            frame_delta,
            int(self.camera.sensitivity_threshold),
            255,
            cv2.THRESH_BINARY,
        )[1]
        thresh = cv2.dilate(thresh, None, iterations=2)
        contours, _ = cv2.findContours(
            thresh.copy(),
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE,
        )

        for contour in contours:
            if cv2.contourArea(contour) < int(self.camera.min_area):
                continue

            motion_detected = True
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(annotated_frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(
                annotated_frame,
                "MOTION DETECTED",
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                2,
            )

        self.previous_gray = gray
        return annotated_frame, motion_detected

    def save_motion_event(self):
        MotionEvent.objects.create(
            camera=self.camera,
            message="Движение засечено",
        )
        self.last_motion_at = timezone.now()

    def generate_mjpeg(self) -> Generator[bytes, None, None]:
        status = self.open()
        if not status.connected:
            raise RuntimeError(status.error or "Невъзможно е да се стартира потокът.")

        try:
            while True:
                start_time = time.time()
                frame = self.read_frame()
                if frame is None:
                    raise RuntimeError("Потокът е прекъснат или няма кадри от камерата.")

                annotated_frame, motion_detected = self.process_motion(frame)

                if motion_detected:
                    if self.last_motion_at is None or (timezone.now() - self.last_motion_at).total_seconds() > 2:
                        self.save_motion_event()

                success, buffer = cv2.imencode(".jpg", annotated_frame)
                if not success:
                    continue

                _fps = 1.0 / max(time.time() - start_time, 0.0001)

                yield (
                    b"--frame\r\n"
                    b"Content-Type: image/jpeg\r\n\r\n" + buffer.tobytes() + b"\r\n"
                )

        finally:
            self.close()

    def get_status(self) -> StreamStatus:
        status = self.open()
        if not status.connected:
            return status

        start_time = time.time()
        frame = self.read_frame()
        if frame is None:
            self.close()
            return StreamStatus(connected=False, error="Няма входящи кадри.")

        elapsed = time.time() - start_time
        fps = 1.0 / max(elapsed, 0.0001)

        self.close()
        return StreamStatus(connected=True, fps=fps, latency_ms=elapsed * 1000)