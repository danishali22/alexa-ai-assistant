import cv2
import base64
from dotenv import load_dotenv

load_dotenv()

def capture_image() -> str:
    """
    Captures one frame from the default webcam, resizes it,
    encodes it as Base64 JPEG (raw string) and returns it.
    """
    for idx in range(4):
        # cap = cv2.VideoCapture(idx, cv2.CAP_AVFOUNDATION)
        cap = cv2.VideoCapture(idx, cv2.CAP_V4L2)

        if cap.isOpened():
            for _ in range(10):  # Warm up
                cap.read()
            ret, frame = cap.read()
            cap.release()
            if not ret:
                continue
            cv2.imwrite("sample.jpg", frame)  # Optional
            ret, buf = cv2.imencode('.jpg', frame)
            if ret:
                return base64.b64encode(buf).decode('utf-8')
    raise RuntimeError("Could not open any webcam (tried indices 0-3)")

capture_image()