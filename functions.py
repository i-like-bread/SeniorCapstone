import pyautogui
from pynput import keyboard

def mousePositionClick():
    completed()
    mousePos = pyautogui.position()
    print(mousePos)
    pyautogui.click(mousePos)

#ToDo: listen for keyboard input
#def keyboardInput():

def on_press(key):
    print("pressed enter")

def on_release(key):
    if(key == keyboard.Key.enter):
        print("Released Enter")
        return False  


def completed():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    