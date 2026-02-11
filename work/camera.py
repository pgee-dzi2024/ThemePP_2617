import cv2
import threading
import time
from flask import Flask, Response, render_template

app = Flask(__name__)

# Настройки
CAMERA_INDEX = 0            # 0 за вградена/първа камера, или rtsp/ваш поток
FRAME_WIDTH = 640
FRAME_HEIGHT = 480
FPS = 20

# Споделени променливи
output_frame = None
lock = threading.Lock()
motion_detected = False

def camera_thread(src=CAMERA_INDEX):
    global output_frame, motion_detected
    cap = cv2.VideoCapture(src)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)
    cap.set(cv2.CAP_PROP_FPS, FPS)

    # Първи кадър за сравнение
    ret, prev = cap.read()
    if not ret:
        print("Не може да отвори камера/поток:", src)
        return
    prev_gray = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)
    prev_gray = cv2.GaussianBlur(prev_gray, (21, 21), 0)

    while True:
        ret, frame = cap.read()
        if not ret:
            # пауза и опит за повторно свързване
            time.sleep(0.5)
            continue

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        # Разлика между кадри
        frame_delta = cv2.absdiff(prev_gray, gray)
        thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)

        # Намираме контури (движение)
        contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        motion = False
        for c in contours:
            if cv2.contourArea(c) < 500:  # праг за минимална площ
                continue
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            motion = True

        motion_detected = motion

        # Добавяме текст на кадъра
        status_text = "Motion" if motion else "No Motion"
        cv2.putText(frame, status_text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                    (0, 0, 255) if motion else (0, 255, 0), 2)

        # Запазваме настоящия кадър като output_frame (JPEG)
        with lock:
            output_frame = frame.copy()

        # Настоящия кадър става предишен
        prev_gray = gray

        # регулируем fps
        time.sleep(1.0 / FPS)

    cap.release()

    def generate_mjpeg():
        global output_frame
        while True:
            with lock:
                if output_frame is None:
                    continue
                # Кодираме кадъра в JPEG
                ret, jpeg = cv2.imencode('.jpg', output_frame)
                if not ret:
                    continue
                frame_bytes = jpeg.tobytes()

            # MJPEG рамка
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
            time.sleep(0.001)

    @app.route('/video_feed')
    def video_feed():
        return Response(generate_mjpeg(),
                        mimetype='multipart/x-mixed-replace; boundary=frame')

    @app.route('/')
    def index():
        # шаблонът показва img към /video_feed и индикация за движение (чрез AJAX)
        return render_template('index.html')

    @app.route('/motion_status')
    def motion_status():
        # връща прост текст (може да е JSON)
        return ("1" if motion_detected else "0"), 200, {'Content-Type': 'text/plain'}