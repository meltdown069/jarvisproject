import config
from google import genai
import pytesseract
import speech_recognition as sr
from PIL import Image
import pyautogui

def test_all():
    print("--- JARVIS SYSTEM CHECK ---")

    # 1. Test Gemini
    try:
        client = genai.Client(api_key=config.GEMINI_KEY)
        response = client.models.generate_content(model="gemini-2.0-flash", contents="Say 'Neural link active'")
        print(f"[SUCCESS] Gemini: {response.text}")
    except Exception as e:
        print(f"[FAILED] Gemini API: {e}")

    # 2. Test Tesseract (OCR)
    try:
        pytesseract.pytesseract.tesseract_cmd = config.TESSERACT_PATH
        # Try to read a tiny part of the screen
        pyautogui.screenshot("test_scan.png", region=(0, 0, 300, 300))
        text = pytesseract.image_to_string(Image.open("test_scan.png"))
        print(f"[SUCCESS] Tesseract: Eyes are functional.")
    except Exception as e:
        print(f"[FAILED] Tesseract OCR: Ensure path in config.py is correct. Error: {e}")

    # 3. Test Microphone
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Please say 'Hello' to test your mic...")
            audio = r.listen(source, timeout=3)
            word = r.recognize_google(audio)
            print(f"[SUCCESS] Microphone: Heard '{word}'")
    except Exception as e:
        print(f"[FAILED] Microphone/Speech: {e}")

if __name__ == "__main__":
    test_all()