import pyautogui
import pytesseract
import config

# Pointing to the Tesseract exe from your config file
pytesseract.pytesseract.tesseract_cmd = config.TESSERACT_PATH

def scan_screen():
    """Takes a screenshot and converts images of text into a string."""
    try:
        # Take a screenshot of the entire primary monitor
        screenshot = pyautogui.screenshot()
        # Extract text from the image
        text = pytesseract.image_to_string(screenshot)
        return text.strip()
    except Exception as e:
        return f"Error scanning screen: {e}"