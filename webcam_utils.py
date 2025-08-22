import cv2

camera = None
last_frame = None
is_running = False

def initialize_camera():
    """Initialize the camera once with optimized settings"""
    global camera
    if camera is None:
        camera = cv2.VideoCapture(0, cv2.CAP_V4L2)  # V4L2 backend for Linux
        if camera.isOpened():
            camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            camera.set(cv2.CAP_PROP_FPS, 30)
            camera.set(cv2.CAP_PROP_BUFFERSIZE, 1)
    return camera is not None and camera.isOpened()

def start_webcam():
    """Start the webcam (used by Gradio UI)"""
    global is_running
    if initialize_camera():
        is_running = True
    return get_webcam_frame()

def stop_webcam():
    """Release the webcam"""
    global is_running, camera
    is_running = False
    if camera is not None:
        camera.release()
        camera = None
    return None

def get_webcam_frame():
    """Get latest webcam frame (RGB)"""
    global camera, last_frame
    if camera is None or not camera.isOpened():
        return last_frame

    ret, frame = camera.read()
    if ret:
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        last_frame = frame_rgb
        return frame_rgb
    return last_frame

def capture_current_frame(save_path="webcam.jpg"):
    """Capture and save one frame from the already running webcam"""
    global last_frame, is_running, camera

    if is_running and last_frame is not None:
        # Reuse the latest frame from running stream
        cv2.imwrite(save_path, cv2.cvtColor(last_frame, cv2.COLOR_RGB2BGR))
        return save_path

    # Webcam not running → cannot capture (do not try to open a new camera)
    print("Webcam not running, cannot capture frame")
    return None

