from google import genai
import config

# Initialize Gemini Client
client = genai.Client(api_key=config.GEMINI_KEY)

def ask_jarvis(prompt):
    try:
        # We use 'gemini-2.0-flash' because it's fast and free
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=f"You are JARVIS from Iron Man. Keep replies brief and professional. User says: {prompt}"
        )
        return response.text
    except Exception as e:
        return f"Sir, my neural core is experiencing an error: {e}"