import pyautogui
# import pynput
import keyboard
import time
# import re


#listen for keyboard input from user: enter, w, m, or k
def prompt_user():
    print("in prompt user")
    key = keyboard.read_key()
    if(key == 'c'):
        print("\n'c' was pressed: Continuing")
        return "Continue"
    elif(key == 'w'):
        print("\n'w' was pressed: Waiting")
        return waitInput()
    elif(key == 'm'):
        print("\n'm' was pressed: MouseClick\nPress Enter to get MouseClick Coords")
        return mouseClickInput()
    elif(key == 'k'):
        print("\n'k' was pressed: KeyboardInput")
        return keyboardInput()
    else:
        print("Try Again")
        return prompt_user()


#wait for specified amount of time
def waitInput():
    waitTime = input("Enter amount of time to wait (Enter to finish): ")
    waitTuple = tuple(('Wait', waitTime))
    print(waitTuple)
    return waitTuple


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
    keys = keyboard.record(until="esc")
    keyboardInputTuple = ("KeyboardInput", keys)
    print(keyboardInputTuple)
    #keyboard.play(keys)
    return keyboardInputTuple


# testValue = prompt_user()

def perform_action(testValue):

    if(testValue[0] == 'Continue'):
        return
    elif(testValue[0] == 'MouseClick'):
        x = testValue[1][0]
        y = testValue[1][1]
        print(f"Moving mouse to {x},{y}")
        pyautogui.moveTo(x, y)
        time.sleep(3)
        # pyautogui.rightClick()
    elif(testValue[0] == 'KeyboardInput'):
        keyboard.play(testValue[1])
    elif(testValue[0] == 'Wait'):
        time.sleep(int(testValue[1][0]))

#perform_action()
