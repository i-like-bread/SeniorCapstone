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
        return promptUser()
        


#ToDo: Allow input when not in console (eg. like keyboard input); maybe just call keyboardInput?
#wait for specified amount of time
def waitInput():
    waitTime = input("Enter amount of time to wait (Enter to finish): ")
    waitTuple = ("Wait", waitTime)
    print(waitTuple)
    time.sleep(1)
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
        time.sleep(1)
        return mouseClickTuple
    else:
        return mouseClickInput()
        



def keyboardInput():
    keys = input("Enter keys/text to input (Enter to finish): ")
    keyboardInputTuple = ("KeyboardInput", keys)
    print(keyboardInputTuple)
    time.sleep(1)
    return keyboardInputTuple
