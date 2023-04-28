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
        return "'continue'"
    elif(key == 'm'):
        print("\n'm' was pressed: mouse_input\nPress esc to get coords")
        return mouse_input()
    elif(key == 'k'):
        print("\n'k' was pressed: keyboard_input")
        return keyboard_input()
    else:
        print("Try Again")
        return prompt_user()


#get mouse coords and click
def mouse_input():
    key = keyboard.read_key()
    if(key == 'esc'):
        #get current mouse position
        mouse_pos = pyautogui.position()
        #pass coords to print
        coords = tuple((mouse_pos.x, mouse_pos.y))
        mouse_click_tuple = ("mouse_input", coords)
        print(mouse_click_tuple)
        return mouse_click_tuple
    else:
        return mouse_input()
        
#get keys
def keyboard_input():
    #reads the k key from user selection, is dead code
    keyboard.read_key()
    #records keys
    key_events = (keyboard.record(until="esc"))
    key_strings = list(keyboard.get_typed_strings(key_events))
    keyboard_input_tuple = ("keyboard_input", key_strings[0])
    print(keyboard_input_tuple)
    return keyboard_input_tuple


def perform_action(test_value):
    #continue
    if(test_value == 'continue'):
        return
    #move mouse and click
    elif(test_value[0] == 'mouse_input'):
        x = test_value[1][0]
        y = test_value[1][1]
        print(f"Moving mouse to {x},{y}")
        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(3)
    #playback keys
    elif(test_value[0] == 'keyboard_input'):
        print((test_value[1]))
        keyboard.write(test_value[1])
        time.sleep(3)
