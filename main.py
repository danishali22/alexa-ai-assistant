import os
import gradio as gr
from speech_to_text import record_audio, transcribe_with_groq
from ai_agent import ask_agent
from text_to_speech import text_to_speech_with_elevenlabs, text_to_speech_with_gtts
from webcam_utils import start_webcam, stop_webcam, get_webcam_frame

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
audio_filepath = "audio_question.mp3"

def process_audio_and_chat():
    chat_history = []
    while True:
        try:
            record_audio(file_path=audio_filepath)
            # user_input = "Do I have a beard?"
            user_input = transcribe_with_groq(audio_filepath)

            if "goodbye" in user_input.lower():
                break

            response = ask_agent(user_query=user_input)

            print("response", response)

            text_to_speech_with_elevenlabs(input_text=response, output_filepath="final.mp3")

            chat_history.append([user_input, response])

            yield chat_history

        except Exception as e:
            print(f"Error in continuous recording: {e}")
            break

# Code for frontend
import cv2
# Global variables
camera = None
is_running = False
last_frame = None

with gr.Blocks() as demo:
    gr.Markdown("<h1 style='color: orange; text-align: center;  font-size: 4em;'> 👧🏼 Alexa – Your Personal AI Assistant</h1>")

    with gr.Row():
        # Left column - Webcam
        with gr.Column(scale=1):
            gr.Markdown("## Webcam Feed")
            
            with gr.Row():
                start_btn = gr.Button("Start Camera", variant="primary")
                stop_btn = gr.Button("Stop Camera", variant="secondary")
            
            webcam_output = gr.Image(
                label="Live Feed",
                streaming=True,
                show_label=False,
                width=640,
                height=480
            )
            
            # Faster refresh rate for smoother video
            webcam_timer = gr.Timer(0.033)  # ~30 FPS (1/30 ≈ 0.033 seconds)
        
        # Right column - Chat
        with gr.Column(scale=1):
            gr.Markdown("## Chat Interface")
            
            chatbot = gr.Chatbot(
                label="Conversation",
                height=400,
                show_label=False
            )
            
            gr.Markdown("*🎤 Continuous listening mode is active - speak anytime!*")
            
            with gr.Row():
                clear_btn = gr.Button("Clear Chat", variant="secondary")
    
    # Event handlers
    start_btn.click(
        fn=start_webcam,
        outputs=webcam_output
    )
    
    stop_btn.click(
        fn=stop_webcam,
        outputs=webcam_output
    )
    
    webcam_timer.tick(
        fn=get_webcam_frame,
        outputs=webcam_output,
        show_progress=False  # Hide progress indicator for smoother experience
    )
    
    clear_btn.click(
        fn=lambda: [],
        outputs=chatbot
    )
    
    # Auto-start continuous mode when the app loads
    demo.load(
        fn=process_audio_and_chat,
        outputs=chatbot
    )

## Launch the app
if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=True,
        debug=True
    )