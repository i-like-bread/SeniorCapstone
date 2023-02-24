import pyautogui
from pynput import keyboard
import time



#listen for keyboard input from user; print pressed keys until user hits enter
def promptUser():
    with keyboard.Listener(on_press=on_press_key, on_release=on_release_key) as listener:
        listener.join()

def on_press_key(key):
    print("")

#ToDo: Add wait functionality
def on_release_key(key):
    if(key == keyboard.Key.enter):
        print(key,"was pressed: Continued")
        return False
    elif(key.char == 'w'):
        print(key,"was pressed: Waiting")
        #ToDo: Fix
        #waitInput(key)
    elif(key.char == 'm'):
        print(key,"was pressed: MouseClick")
        mouseClickInput()
    elif(key.char == 'k'):
        print(key,"was pressed: KeyboardInput")
        keyboardInput()
    else:
        print(key,"is invalid, try again")


def waitInput(key):
    print("Wait",key)
    #time.sleep(int(key))



#get MouseClick coords
def mouseClickInput():
    #if user hits enter
    action()
    #get current mouse position
    mousePos = pyautogui.position()
    #pass coords to print
    (x, y) = (mousePos.x, mousePos.y)
    print("MouseClick at", (x, y))
    #click at the current position
    pyautogui.click(mousePos)

#ToDo: join printed chars together into a string
def keyboardInput():
    action()


#listen until enter key is hit; basically a "continue once user hits enter" method
#used to allow user to move mouse until they hit enter
def action():
    with keyboard.Listener(on_press=on_press, on_release=on_release_enter) as listener:
        listener.join()

def on_press(key):
    print(key)

def on_release_enter(key):
    if(key == keyboard.Key.enter):
        print("Released Enter (Completed Action)")
        return False