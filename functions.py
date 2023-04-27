import pyautogui
# import pynput
import keyboard
import time
# import re


#listen for keyboard input from user: c, m, or k
def prompt_user():
    print("Press 'c' to continue, 'm' to move mouse, or 'k' to press keys")
    key = keyboard.read_key()
    if(key == 'c'):
        print("\n'c' was pressed: Continuing")
        return "'Continue'"
    elif(key == 'm'):
        print("\n'm' was pressed: MouseClick\nPress Enter to get MouseClick Coords")
        return mouseClickInput()
    elif(key == 'k'):
        print("\n'k' was pressed: KeyboardInput")
        return keyboardInput()
    else:
        print("Try Again")
        return prompt_user()


#get MouseClick coords and click
def mouseClickInput():
    key = keyboard.read_key()
    if(key == 'enter'):
        #get current mouse position
        mousePos = pyautogui.position()
        #pass coords to print
        coords = tuple((mousePos.x, mousePos.y))
        mouseClickTuple = ("MouseClick", coords)
        print(mouseClickTuple)
        return mouseClickTuple
    else:
        return mouseClickInput()
        

def keyboardInput():
    #reads the k key from user selection, is dead code
    keyboard.read_key()

    #records keys
    key_events = (keyboard.record(until="esc"))
    key_strings = list(keyboard.get_typed_strings(key_events))
    keyboardInputTuple = ("KeyboardInput", key_strings[0])
    print(keyboardInputTuple)
    return keyboardInputTuple


def perform_action(testValue):

    if(testValue == 'Continue'):
        return
    elif(testValue[0] == 'MouseClick'):
        x = testValue[1][0]
        y = testValue[1][1]
        print(f"Moving mouse to {x},{y}")
        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(3)
    elif(testValue[0] == 'KeyboardInput'):
        print((testValue[1]))
        keyboard.write(testValue[1])
        time.sleep(3)
