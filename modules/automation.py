import pyautogui
import keyboard
import os

def check_kill_switch():
    # Immediate shutdown if keys are pressed
    if keyboard.is_pressed('f1+f2+f3'):
        print("!!! EMERGENCY SHUTDOWN !!!")
        os._exit(0)

def open_app(app_name):
    pyautogui.press('win')
    pyautogui.write(app_name, interval=0.1)
    pyautogui.press('enter')