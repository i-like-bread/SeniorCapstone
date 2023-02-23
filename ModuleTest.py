from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, MoveTargetOutOfBoundsException


import time
from pynput import keyboard

# When call this function, press 1 or 2 twice to able to run the script, when calling it make sure it have like this prompt_user('0')

       
def prompt_user(key):
          
    try:
        
        # Convert the key to a string
        key_str = str(key.char)
        # Check if the key is between 1 and 2
        if '1' <= key_str <= '2':
            # Print the key
            
            print(key_str)
            
            
            while True:
    
                time.sleep(5)
        
                if key_str == '1':
            
                    print('Continuing')
                    break
        
                if key_str == '2':

                    print('Pausing for 5 seconds')

                    time.sleep(5)
            
                    break
                       
                else :
            
                    print("Invalid input")
            
            # Stop listening to key events
            return False
         
    except AttributeError:
        # Ignore special keys like 'ctrl', 'shift', etc.
        pass
    
# Create a keyboard listener
listener = keyboard.Listener(on_press=prompt_user)
# Start the listener
listener.start()
# Wait for the listener to stop (when a key between 1 and 2 is pressed)
listener.join()





# Team 2 (two person team): Write a function as a separate Python module.  This function will:
# Ask the user if they want to: 
# (1) Continue to the next step, 
# (2) Pause for a certain number of seconds, 
# or (2) Move the cursor to a certain location (and then hit return so you know they have done it).
# Work with Team 3 on what this function should return.
