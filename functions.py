import pyautogui
import pynput
import keyboard
import time
import re


#listen for keyboard input from user: enter, w, m, or k
def promptUser():
    key = keyboard.read_key()
    if(key == 'c'):
        print("\n'c' was pressed: Continuing")
        return "Continue"
    elif(key == 'w'):
        keyboard.read_key()
        print("\n'w' was pressed: Waiting")
        return waitInput()
    elif(key == 'm'):
        keyboard.read_key()
        print("\n'm' was pressed: MouseClick\nPress Enter to get MouseClick Coords")
        return mouseClickInput()
    elif(key == 'k'):
        keyboard.read_key()
        print("\n'k' was pressed: KeyboardInput")
        return keyboardInput()
    else:
        print("Try Again")
        return promptUser()


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


testValue = promptUser()

def performAction(testValue, input):
    if(testValue == 'Continue'):
        return
    elif(testValue[0] == 'MouseClick'):
        pyautogui.moveTo(input)
        pyautogui.rightClick()
    elif(testValue[0] == 'KeyboardInput'):
        keyboard.play(input)
    elif(testValue[0] == 'Wait'):
        time.sleep(int(input))
