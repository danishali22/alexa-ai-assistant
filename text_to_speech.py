import os
import elevenlabs
from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv
import subprocess
import platform
from gtts import gTTS

load_dotenv()

ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")


def play_audio_file(output_filepath):
    """Play audio file depending on OS"""
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run([
                'powershell', '-c',
                f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'
            ])
        elif os_name == "Linux":  # Linux
            # Prefer mpg123/ffplay for MP3, fallback to aplay for WAV
            if output_filepath.endswith(".mp3"):
                subprocess.run(['mpg123', output_filepath])
            else:
                subprocess.run(['aplay', output_filepath])
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")


def text_to_speech_with_elevenlabs(input_text, output_filepath=None):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

    audio = client.text_to_speech.convert(
        text=input_text,
        voice_id="ZF6FPAbjXT4488VcRRnw",
        model_id="eleven_multilingual_v2",
        output_format="mp3_22050_32",
    )
    if output_filepath is None:
        output_filepath = "output.mp3"
    elevenlabs.save(audio, output_filepath)
    play_audio_file(output_filepath)


def text_to_speech_with_gtts(input_text, output_filepath="output_gtts.mp3"):
    language = "en"
    audioobj = gTTS(text=input_text, lang=language, slow=False)
    audioobj.save(output_filepath)
    play_audio_file(output_filepath)

# input_text = "Hi, I am doing fine, how are you? This is a test for Danish Ali"

# ✅ Offline save + play (MP3)
# text_to_speech_with_elevenlabs(input_text, "test_elevenlabs.mp3")

# ✅ gTTS example
# text_to_speech_with_gtts(input_text, "test_gtts.mp3")
