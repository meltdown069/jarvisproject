
# 🦾 JARVIS: v2.0

| **Model:** Google Gemini 2.0 Flash | **Tier:** Free 

JARVIS is a minimalist, voice-active AI desktop companion designed for seamless human-computer interaction. By stripping away the clutter of traditional terminal logs, the Neural Core v2.0 focuses on a sleek, "ambient" interface that manages intelligence, automation, and API health in real-time.

---

## ⚡ Core Systems

* **🎙️ Whisper-Quiet Listening:** High-sensitivity voice engine tuned for "Jarvis" wake-word detection.
* **⌨️ Hybrid Input:** A minimalist command bar for silent operation when voice isn't an option.
* **🔋 Quota Guardian:** A visual "Neural Lamp" that prevents API crashes by monitoring Gemini Free Tier rate limits (429 errors).
* **🚀 Smart Automation:** Natural language application launching and system-level task execution.
* **🧠 Deep Context:** Powered by Gemini 2.0 Flash for low-latency, high-intelligence responses.

---

## 📂 Project Architecture

```text
jarvisproject/
├── main.py              # The "Central Nervous System" (Threading & Logic)
├── modules/
│   ├── gui.py           # The "Face" (Minimalist Tkinter UI & Neural Lamp)
│   ├── ai_engine.py     # The "Intelligence" (Gemini Pro API Bridge)
│   ├── automation.py    # The "Limbs" (App Control & System OS)
│   └── vision.py        # The "Eyes" (Screen OCR & Vision capabilities)
├── config.py            # System Credentials & Environment Keys
└── README.md            # System Manual

```

---

## 🛠️ Deployment Protocol

### 1. Environmental Requirements

* **Python:** 3.10 or higher.
* **API Access:** A valid API Key from [Google AI Studio](https://aistudio.google.com/).

### 2. Initialization

Install the required neural dependencies via your terminal:

```bash
pip install speechrecognition pyttsx3 google-generativeai keyboard pyaudio

```

### 3. Neural Calibration

Update `config.py` with your unique identifier:

```python
# config.py
GEMINI_API_KEY = "YOUR_API_KEY_HERE"

```

### 4. Boot Sequence

```bash
python main.py

```

---

## 🚥 Visual Telemetry (Neural Lamp)

The Neural Lamp at the top of the interface provides real-time feedback on JARVIS's current state:

| Lamp Color | System State | Description |
| --- | --- | --- |
| 🟢 **Cyan/Green** | **IDLE** | System is ready and listening for the "Jarvis" wake-word. |
| 🟡 **Yellow** | **THINKING** | Gemini is processing your request via the cloud. |
| 🟣 **Magenta** | **SPEAKING** | Text-to-speech engine is currently active. |
| 🔴 **Red** | **COOLDOWN** | API Rate Limit (429) reached. System is locked for 60s. |

---

## ⌨️ Tactical Shortcuts

* **Enter Key:** Submit manual commands instantly.
* **F1 + F2 + F3:** Hard Shutdown (Emergency Kill Switch).

---

## 🔗 Connect With Me

Stay updated with the latest neural core developments:

* **Instagram:** [fire.drgon](https://www.google.com/search?q=https://instagram.com/fire.drgon)

---

## 📄 Licensing

This core is open-source. **"Sometimes you gotta run before you can walk."** Feel free to fork, modify, and improve.

---

**⚠️ UNDER DEVELOPMENT**
