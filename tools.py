import base64
import cv2
from dotenv import load_dotenv
from webcam_utils import capture_current_frame
from groq import Groq

load_dotenv()

def capture_image() -> str:
    """
    Captures one frame from the already running webcam
    (managed by main.py) and encodes it as Base64 JPEG string.
    """
    img_path = capture_current_frame()
    if not img_path:
        raise RuntimeError("Could not capture image from active webcam")

    frame = cv2.imread(img_path)
    if frame is None:
        raise RuntimeError("Failed to read captured image file")

    ret, buf = cv2.imencode('.jpg', frame)
    if not ret:
        raise RuntimeError("Failed to encode image to JPEG")

    return base64.b64encode(buf).decode('utf-8')


def analyze_image_with_query(query: str) -> str:
    """
    Takes the current webcam frame and sends it with the query
    to Groq's vision chat API for analysis.
    """
    img_b64 = capture_image()
    model = "meta-llama/llama-4-maverick-17b-128e-instruct"
    
    if not query or not img_b64:
        return "Error: both 'query' and 'image' fields required."

    client = Groq()
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": query},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{img_b64}",
                    },
                },
            ],
        }
    ]

    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model
    )

    return chat_completion.choices[0].message.content
