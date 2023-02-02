from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import time
from getpass import getpass
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

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

# enter iframe
iframe = driver.find_element(By.XPATH, '//*[@id="cyrinFrame"]')
driver.switch_to.frame(iframe)

# if the exercise hasn't started, checked for by the Training Scenario heading,
# throwing errors here
try:
    if driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/h2'):
        #find the start exercise button and click
        driver.find_element(By.XPATH, '//*[@id="launch-actions"]/form/input[4]').click()
        #switch back to original iframe
        # driver.switch_to.default_content()
except NoSuchElementException:
    pass



# switch from Computer C to Computer A (outside of the vm):
#find CYRIN iframe and switch to it
# iframe = driver.find_element(By.XPATH, '//*[@id="cyrinFrame"]')
# driver.switch_to.frame(iframe)


# issue - waiting for the exercise to finish starting up takes a long time
# wait for the vm to load
time.sleep(10)

# couldn't find the button
driver.find_element(By.XPATH, '//*[@id="computersMenuButton"]]').click()
driver.find_element(By.XPATH, '//*[@id="displaymachine1_Ubuntu2004Desktop-4000-0182-eba4edce-809a-3fe20a37e1aa"]').click()





# inside the vm: open the terminal




#switch back to original iframe code
# driver.switch_to.default_content()

# end the exercise via button in iframe
# driver.switch_to.frame(driver.find_element(By.XPATH, '//iframe[@id = "cyrinFrame"]'))
# driver.find_element(By.XPATH, "//button[@id = 'btnEndExercise']").click()
# time.sleep(5)
# driver.find_element(By.XPATH, "//button[@id = 'btnConfirmEndExercise']").click()

#close driver
# driver.close()
