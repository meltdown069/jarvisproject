import threading
import time
import speech_recognition as sr
import pyttsx3
import os
import keyboard
from modules import gui, automation, ai_engine

# Initialize Voice
engine = pyttsx3.init()
engine.setProperty('rate', 190) 

def speak(text):
    if not text: return
    jarvis_window.update_status("Speaking...", color="#bb86fc", lamp_color="#bb86fc")
    engine.say(text)
    engine.runAndWait()
    jarvis_window.update_status("System Ready", color="#00d4ff", lamp_color="#00ffcc")

def run_cooldown(seconds):
    """Prevents crashing during Gemini 429 errors"""
    for i in range(seconds, 0, -1):
        jarvis_window.update_status(f"QUOTA FULL: {i}s", color="#cf6679", lamp_color="#cf6679")
        time.sleep(1)
    jarvis_window.update_status("SYSTEM READY", color="#00d4ff", lamp_color="#00ffcc")

def handle_logic(command):
    if not command: return
    jarvis_window.update_status("Thinking...", color="#f4ff81", lamp_color="#f4ff81")
    
    try:
        if "open" in command:
            app = command.replace("open ", "").strip()
            automation.open_app(app)
            speak(f"Accessing {app} for you, sir.")
        else:
            response = ai_engine.ask_jarvis(command)
            speak(response)
    except Exception as e:
        if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
            threading.Thread(target=run_cooldown, args=(60,), daemon=True).start()
        else:
            jarvis_window.log(f"Logic Error: {e}")
            jarvis_window.update_status("System Error", color="red", lamp_color="red")

def listen():
    r = sr.Recognizer()
    r.energy_threshold = 300 
    r.dynamic_energy_threshold = False
    with sr.Microphone() as source:
        try:
            audio = r.listen(source, timeout=2, phrase_time_limit=4)
            return r.recognize_google(audio).lower()
        except: return ""

def jarvis_brain():
    while True:
        if keyboard.is_pressed('f1+f2+f3'): os._exit(0)
        voice_input = listen()
        if "jarvis" in voice_input:
            speak("Yes sir?")
            cmd = listen()
            if cmd: handle_logic(cmd)
        time.sleep(0.4)

if __name__ == "__main__":
    jarvis_window = gui.JarvisGUI(handle_logic)
    threading.Thread(target=jarvis_brain, daemon=True).start()
    jarvis_window.root.mainloop()