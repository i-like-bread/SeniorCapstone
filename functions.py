import pyautogui
import pynput
import keyboard
import time



#listen for keyboard input from user: enter, w, m, or k
def promptUser():
    key = keyboard.read_key()
    if(key == 'c'):
        print("'Enter' was pressed: Continuing")
        time.sleep(1)
    elif(key == 'w'):
        print("'w' was pressed: Waiting")
        waitInput()
    elif(key == 'm'):
        print("'m' was pressed: MouseClick")
        mouseClickInput()
    elif(key == 'k'):
        print("'k' was pressed: KeyboardInput")
        keyboardInput()
    else:
        print("Try Again")
        promptUser()



#ToDo: Allow input when not in console (eg. like keyboard input); maybe just call keyboardInput?
#wait for specified amount of time
def waitInput():
    waitTime = input("Enter amount of time to wait: ")
    waitTuple = ("Wait", waitTime)
    print(waitTuple)
    time.sleep(1)



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
    else:
        mouseClickInput()



def keyboardInput():
    keys = input("Enter keys/text to input: ")
    keyboardInputTuple = ("KeyboardInput", keys)
    print(keyboardInputTuple)
    time.sleep(1)
