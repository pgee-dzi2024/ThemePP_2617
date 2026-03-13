import cv2
import threading
import time
from flask import Flask, Response

app = Flask(__name__)

# Settings
CAMERA_INDEX = 0
FRAME_WIDTH = 640
FRAME_HEIGHT = 480
FPS = 20

output_frame = None
lock = threading.Lock()
motion_detected = False


def camera_thread(src=CAMERA_INDEX):
    global output_frame, motion_detected

    cap = cv2.VideoCapture(src)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

    ret, prev = cap.read()
    if not ret:
        print("Cannot open camera")
        return

    prev_gray = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)
    prev_gray = cv2.GaussianBlur(prev_gray, (21, 21), 0)

    while True:
        ret, frame = cap.read()
        if not ret:
            time.sleep(0.5)
            continue

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        frame_delta = cv2.absdiff(prev_gray, gray)
        thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)

        contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        motion = False

        for c in contours:
            if cv2.contourArea(c) < 500:
                continue

            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
            motion = True

        motion_detected = motion

        status = "Motion" if motion else "No Motion"

        cv2.putText(frame, status, (10,30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0,0,255) if motion else (0,255,0),
                    2)

        with lock:
            output_frame = frame.copy()

        prev_gray = gray

        time.sleep(1/FPS)


def generate():
    global output_frame

    while True:
        with lock:
            if output_frame is None:
                continue

            ret, buffer = cv2.imencode('.jpg', output_frame)
            frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

        time.sleep(0.01)


@app.route('/')
def index():
    return """
    <html>
    <head>
    <title>Camera Motion Detection</title>
    </head>
    <body>
        <h2>Live Camera Stream</h2>
        <img src="/video_feed" width="640">
    </body>
    </html>
    """


@app.route('/video_feed')
def video_feed():
    return Response(generate(),
        mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/motion_status')
def motion_status():
    return "1" if motion_detected else "0"


if __name__ == "__main__":

    t = threading.Thread(target=camera_thread)
    t.daemon = True
    t.start()

    app.run(host="0.0.0.0", port=5000, threaded=True)