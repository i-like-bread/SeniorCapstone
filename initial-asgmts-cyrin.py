from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from getpass import getpass
import time

# prompt for username and password
username = input("Username: ")
password = getpass()

# open Chrome
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

# if the exercise hasn't started,
# currently the exercise assumes it has already been started
try:
    #  check for the Training Scenario heading
    # throwing errors here
    # maybe include a check for specific text?
    if driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/h2'):
        #find the start exercise button and click
        driver.find_element(By.XPATH, '//*[@id="launch-actions"]/form/input[4]').click()
        #switch back to original iframe
        # driver.switch_to.default_content()
except NoSuchElementException:
    pass

driver.switch_to.default_content()

# switch from Computer C to Computer A (outside of the vm):

#find CYRIN iframe and switch to it
iframe = driver.find_element(By.XPATH, '//*[@id="cyrinFrame"]')
driver.switch_to.frame(iframe)


# issue - waiting for the exercise to finish starting up takes a long time
# wait for the vm to load
time.sleep(10)

# switch to Computer A
# driver.find_element(By.XPATH, '//*[@id="computersMenuButton"]').click()
# driver.find_element(By.XPATH, '//*[@id="machinestatus_Ubuntu2004Desktop-4000-0182-eba4edce-809a-3fe20a37e1aa"]').click()

# inside the vm: open the terminal:

# driver.find_element(By.XPATH, '//*[@id="instruction-nav"]/div')

#find the computer screen
#find and click the fullscreen button
# driver.find_element(By.XPATH, '//*[@id="btnToggleFullScreen"]').click()
# ac = ActionChains(driver)
# default coords are top middle
# computerScreen = driver.find_element(By.XPATH, '//*[@id="noVNC_screen"]/div/canvas')
#move to terminal icon and click
# ac.move_to_element_with_offset(computerScreen, -400, 390).context_click().perform()


# Jacob's code
#find and click the fullscreen button
driver.find_element(By.XPATH, '//*[@id="btnToggleFullScreen"]').click()

#find and click computer view button
driver.find_element(By.XPATH, '//*[@id="computersMenuButton"]').click()
#find and click computer A (Ubuntu)
driver.find_element(By.XPATH, '//*[@id="displaymachine1_Ubuntu2004Desktop-4000-0182-eba4edce-809a-3fe20a37e1aa"]').click()

time.sleep(5)

ac = ActionChains(driver)
#find the computer screen
computerScreen = driver.find_element(By.XPATH, '//*[@id="noVNC_screen"]/div/canvas')
#move to terminal icon and click
ac.move_to_element_with_offset(computerScreen, -400, 390).click().perform()






time.sleep(20)

#switch back to original iframe code
# driver.switch_to.default_content()

# end the exercise via button in iframe
# driver.switch_to.frame(driver.find_element(By.XPATH, '//iframe[@id = "cyrinFrame"]'))
# driver.find_element(By.XPATH, "//button[@id = 'btnEndExercise']").click()
# time.sleep(5)
# driver.find_element(By.XPATH, "//button[@id = 'btnConfirmEndExercise']").click()

#close driver
# driver.close()
