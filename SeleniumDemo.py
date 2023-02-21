from selenium import webdriver
from selenium.webdriver.common.by import By
from loginCredentials import login
import functions
import time

#driver goes to CYRIN login
driver = webdriver.Chrome()
driver.get("https://cyrin.atcorp.com/mod/cyrin/view.php?id=166")

#ToDo: Pass login stuff as console input, too lazy to do that now
#username and password fields
username = login.username
password = login.password

#find and input username and password
driver.maximize_window()
driver.find_element(By.ID, "username").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)
#click on login
time.sleep(5)
driver.find_element(By.ID, "loginbtn").click()
time.sleep(5)

#find CYRIN iframe
iframe = driver.find_element(By.XPATH, '//*[@id="cyrinFrame"]')
#switch to iframe
driver.switch_to.frame(iframe)

#find the start button and click
try:
    driver.find_element(By.XPATH, '//*[@id="launch-actions"]/form/input[4]').click()
except:
    print("No Start Button")
time.sleep(5)

#ToDo: If user scrolls and button is not in view, crashes
#find and click computer view button
driver.find_element(By.XPATH, '//*[@id="computersMenuButton"]').click()
#find and click computer A (Ubuntu)
driver.find_element(By.XPATH, '//*[@id="displaymachine1_Ubuntu2004Desktop-4000-0182-eba4edce-809a-3fe20a37e1aa"]').click()
time.sleep(5)

#prompt user to move curser to terminal, click after user hits enter
jsIconAlert = "alert('Please move the mouse curser to the terminal icon on the sidebar within the virtual machine (Press Enter to Finish)')"
driver.execute_script(jsIconAlert)
functions.mousePositionClick()
time.sleep(1)


#prompt user to move curser to terminal window, click after user hits enter
jsWindowAlert = "alert('Please move the mouse curser to the terminal window within the virtual machine (Press Enter to Finish)')"
driver.execute_script(jsWindowAlert)
functions.mousePositionClick()
time.sleep(1)

jsTestAlert = "alert('Testing keyboardInput, will record keys in console (Press Enter to Finish)')"
driver.execute_script(jsTestAlert)
functions.keyboardInput()

#switch back to original iframe
driver.switch_to.default_content()
#close driver
driver.close()
