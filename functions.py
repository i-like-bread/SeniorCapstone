import pyautogui
from pynput import keyboard

def mousePositionClick():
    completed()
    mousePos = pyautogui.position()
    print(mousePos)
    (x, y) = (mousePos.x, mousePos.y)
    print("MouseClick at", (x, y))
    pyautogui.click(mousePos)


def on_press_key(key):
    print("Key Pressed:", key)

def on_release_key(key):
    if(key == keyboard.Key.enter):
        print("Released Enter (Stopping)")
        return False

def keyboardInput():
    with keyboard.Listener(on_press=on_press_key, on_release=on_release_key) as listener:
        listener.join()


def on_press_enter(key):
    print("Pressed Enter")

def on_release_enter(key):
    if(key == keyboard.Key.enter):
        print("Released Enter (Stopping)")
        return False

def completed():
    with keyboard.Listener(on_press=on_press_enter, on_release=on_release_enter) as listener:
        listener.join()