from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import time
from getpass import getpass

# prompt for username and password
username = input("Username: ")
password = getpass()

# import webdriver to open Chrome
from selenium import webdriver
driver = webdriver.Chrome()

# navigate to the website and make it fullscreen
driver.get("https://cyrin.atcorp.com/mod/cyrin/view.php?id=166")
driver.maximize_window()

# navigate to the username box;
# input username, tab to password, input password, then hit enter
driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(username + Keys.TAB + password + Keys.ENTER)

# wait for text to load
time.sleep(5)

# if you are not already in a continuation of the exercise,
# start a new exercise
if driver.find_element(By.XPATH, '//*[@id="cyrinFrame"]') is True:
    #find CYRIN iframe and switch to it
    iframe = driver.find_element(By.XPATH, '//*[@id="cyrinFrame"]')
    driver.switch_to.frame(iframe)
    #find the start button and click
    driver.find_element(By.XPATH, '//*[@id="launch-actions"]/form/input[4]').click()
    #switch back to original iframe
    driver.switch_to.default_content()

# switch from Computer C to Computer A (outside of the vm)



# inside the vm: open the terminal



# end the exercise
driver.switch_to.frame(driver.find_element(By.XPATH, '//iframe[@id = "cyrinFrame"]'))
driver.find_element(By.XPATH, "//button[@id = 'btnEndExercise']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//button[@id = 'btnConfirmEndExercise']").click()

#close driver
driver.close()
