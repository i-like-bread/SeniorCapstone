#Fixed up a bit
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome()
       
def move_and_click(Target):
    
    getTargetClick = driver.find_element(By.XPATH, Target)
    
    action = ActionChains(driver)
    
    action.move_to_element(getTargetClick)\
        .click()\
        .perform()

#Some Funny loop

def time_to_wait():
    
    while True:       
            
        ask_time_wait = input("How many seconds do you want to wait? Enter 0 to exit: ")
    
        try:
                
            ask_time_wait = int(ask_time_wait)
            
            if ask_time_wait == 0:
                
                print('Continuing...')
                break
                                             
        except ValueError:
                
            print("Invalid input. Please enter a valid integer.")
    
        else:
            
            print("Time to wait: " + str(ask_time_wait) + " seconds")    
            time.sleep(ask_time_wait)
                          

def ask_to_pause():
         
    while True:
        
        ask_to_continues = input("Don you want to pause? (y/n) ").lower()
    
        if ask_to_continues == "y":
                              
            time_to_wait()
                     
        elif ask_to_continues == "n":
            
            print('Continuing...')
            break
        
        else:
            print("invalid input")
            
#Funny loop ended here
            
            
#Start forward ask to continues or pause      
def ask_to_pauseB():
    
    while True:
        
        ask_to_continues = input('Do you wanted to pause (y/n)')
        
        if ask_to_continues == "n":
            
            break
        
        elif ask_to_continues == "y"

            print('Pausing for 10s')
            time.sleep(10)
            break
        
        else:
            print('Invalid input')
            
            
        
    
