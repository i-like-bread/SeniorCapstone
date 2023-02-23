import pyautogui
from pynput import keyboard

#get MouseClick coords
def mousePositionClick():
    #if user hits enter
    completed()
    #get current mouse position
    mousePos = pyautogui.position()
    print(mousePos)
    #pass coords to print
    (x, y) = (mousePos.x, mousePos.y)
    print("MouseClick at", (x, y))
    #click at the current position
    pyautogui.click(mousePos)


def on_press_key(key):
    print("Key Pressed:", key)

def on_release_key(key):
    if(key == keyboard.Key.enter):
        print("Released Enter (Stopping)")
        return False

#listen for keyboard input from user; print pressed keys until user hits enter
def keyboardInput():
    with keyboard.Listener(on_press=on_press_key, on_release=on_release_key) as listener:
        listener.join()


def on_press_enter(key):
    print("Pressed Enter")

def on_release_enter(key):
    if(key == keyboard.Key.enter):
        print("Released Enter (Stopping)")
        return False

#listen until enter key is hit; basically a "continue once user hits enter" method
def completed():
    with keyboard.Listener(on_press=on_press_enter, on_release=on_release_enter) as listener:
        listener.join()