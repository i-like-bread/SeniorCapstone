from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, MoveTargetOutOfBoundsException


import time

       
        
def pick_option():
    
    while True:
        
        getInputOption = int(input("Press 1 to continue, Press 2 to pause for 5 seconds"))
    
        time.sleep(5)
        
        if getInputOption == 1:
            
            print('Continuing')
            break
        
        if getInputOption == 2:

            print('Pausing for 5 seconds')

            time.sleep(5)
            
            break
            
            
        else :
            
            print("Invalid input")
            
#The alternative step is kind of hard.  Using driver = webdriver.Chrome() will causes the module to open a blank Chrome Browser.  I think we should find way to automate it without using selenium             
               


# Team 2 (two person team): Write a function as a separate Python module.  This function will:
# Ask the user if they want to: 
# (1) Continue to the next step, 
# (2) Pause for a certain number of seconds, 
# or (2) Move the cursor to a certain location (and then hit return so you know they have done it).
# Work with Team 3 on what this function should return.
