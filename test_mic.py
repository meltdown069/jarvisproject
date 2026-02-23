import speech_recognition as sr

r = sr.Recognizer()
# Change 'None' to your ID if you found one (e.g., device_index=1)
try:
    with sr.Microphone(device_index=None) as source:
        print(">>> Say something clearly...")
        audio = r.listen(source, timeout=5)
        print(">>> Recognizing...")
        print("You said: " + r.recognize_google(audio))
except Exception as e:
    print(f"\n[CRITICAL ERROR]: {e}")
    print("\nTip: If you see 'device_index', try changing 'None' to a number from the list.")