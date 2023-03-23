import pyautogui
#import pynput
import keyboard
import time



#listen for keyboard input from user: enter, w, m, or k
def promptUser():
    key = keyboard.read_key()
    if(key == 'c'):
        print("\n'c' was pressed: Continuing")
        time.sleep(1)
    elif(key == 'w'):
        print("\n'w' was pressed: Waiting")
        waitInput()
        time.sleep(1)
    elif(key == 'm'):
        print("\n'm' was pressed: MouseClick\nPress Enter to get MouseClick Coords")
        mouseClickInput()
        time.sleep(1)
    elif(key == 'k'):
        print("\n'k' was pressed: KeyboardInput")
        keyboardInput()
        time.sleep(1)
    else:
        promptUser()
        time.sleep(1)

"""
    key = keyboard.read_hotkey()
    keyboard.add_hotkey('f1', lambda: print("\n'f1' was pressed: Continuing"))
    keyboard.add_hotkey('f2', waitInput)
    keyboard.add_hotkey('f3', mouseClickInput())
    keyboard.add_hotkey('f4', lambda: keyboardInput)
"""
    



#ToDo: Allow input when not in console (eg. like keyboard input); maybe just call keyboardInput?
#wait for specified amount of time
def waitInput():
    waitTime = input("Enter amount of time to wait (Enter to finish): ")
    waitTuple = ("Wait", waitTime)
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
        return mouseClickTuple
    else:
        mouseClickInput()



def keyboardInput():
    keys = input("Enter keys/text to input (Enter to finish): ")
    keyboardInputTuple = ("KeyboardInput", keys)
    return keyboardInputTuple
