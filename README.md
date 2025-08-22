🤖 Alexa-Style Multimodal AI Assistant
An advanced **multimodal personal AI assistant** that combines **voice, vision, and text** to create an experience similar to Alexa — but smarter. You can **talk to it, show it things through your webcam, and even call it in video form**.

---

📌 Features

* 🎙️ **Voice Input & Transcription**: Converts speech into text using SpeechRecognition + PyAudio.
* 👀 **Webcam & Vision Analysis**: Detects shirt colors, gestures, facial expressions, and objects via OpenCV.
* 🧠 **Agentic RAG**: Handles knowledge retrieval and multi-turn Q\&A with LangGraph + Groq.
* 🔊 **Text-to-Speech (TTS)**: Human-like responses using ElevenLabs and gTTS.
* 🌐 **Multimodal Interface**: Seamlessly supports text, voice, and webcam inputs.
* 🖥️ **Gradio UI**: Interactive web interface for real-time conversations.

---

🛠️ Tech Stack

| Category             | Tools & Services         |
| -------------------- | ------------------------ |
| Programming Language | Python                   |
| UI Framework         | Gradio                   |
| Speech-to-Text       | SpeechRecognition + Groq |
| Vision               | OpenCV                   |
| Text-to-Speech (TTS) | ElevenLabs, gTTS         |
| AI & Orchestration   | LangGraph, Google GenAI  |
| Environment Handling | python-dotenv            |
| Runtime & Packaging  | uv                       |

---

📁 Project Structure

```
└── danishali22-alexa-ai-assistant/
    ├── README.md                # Project documentation
    ├── ai_agent.py              # Agentic RAG + assistant logic
    ├── main.py                  # Entry point with Gradio UI
    ├── pyproject.toml           # Project dependencies & config
    ├── speech_to_text.py        # Speech-to-text pipeline
    ├── text_to_speech.py        # TTS functions (ElevenLabs + gTTS)
    ├── tools.py                 # Utility functions (API calls, env)
    ├── webcam_utils.py          # Webcam capture & analysis
    ├── .python-version          # Python runtime version
    └── .gradio/
        └── certificate.pem      # SSL certificate for Gradio
```

---

🔧 Setup Instructions

**Clone the Repository**

```bash
git clone https://github.com/danishali22/danishali22-alexa-ai-assistant.git
cd danishali22-alexa-ai-assistant
```

**Install Dependencies**

```bash
uv pip install -r pyproject.toml
```

**Configure Environment Variables**

```bash
cp .env.example .env
# Fill in your API keys (Groq, ElevenLabs, etc.)
```

**Run the App**

```bash
python main.py
```

---

🤖 How It Works

1. User interacts via text, voice, or webcam.
2. Voice input is transcribed with SpeechRecognition + Groq.
3. Webcam frames are processed with OpenCV for visual understanding.
4. Knowledge-based responses are generated using Agentic RAG.
5. Replies are returned as text + natural speech (ElevenLabs/gTTS).

---

📚 What I Learned

* Building **multimodal AI** (voice + vision + text)
* Integrating **Groq, LangGraph, and Google GenAI**
* Real-time speech recognition & synthesis
* Creating a smooth **Gradio-powered interface**
* Managing complex dependencies with **uv**

---

🙌 Feedback
If you find this project interesting or want to collaborate, feel free to open an issue or connect!

GitHub: [danishali22](https://github.com/danishali22)
