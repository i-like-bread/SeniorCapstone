from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from getpass import getpass

# Set up username and password
username = input("Username: ")
password = getpass()

# create a browser for selenium
browser = webdriver.Chrome()

# put Chrome in fullscreen
browser.maximize_window()

# Launch Chrome to the Cyrin login
browser.get('https://cyrin.atcorp.com/mod/cyrin/view.php?id=166')

# Select, clear, and then enter username in the username bar
search_bar = browser.find_element(By.XPATH, '//*[@id="username"]')
search_bar.clear()
search_bar.send_keys(username)

# select, clear, and then enter password in the password bar
search_bar = browser.find_element(By.XPATH, '//input[@name = "password"]')
search_bar.clear()
search_bar.send_keys(password)

# selects the login button
search_bar.send_keys(Keys.RETURN)

# wait for the screen to finish loading
time.sleep(7)

# Switch to the iframe that contains the button to start the lab
browser.switch_to.frame(browser.find_element(By.XPATH, '//iframe[@id = "cyrinFrame"]'))

# find the button that starts the lab and click it
object_to_click = browser.find_element(By.XPATH, '//input[@type = "submit"]')
object_to_click.click()

# switch back to the original iframe
browser.switch_to.default_content()

# give the lab some time to load properly
time.sleep(180)

# switch computers to computerA
browser.switch_to.frame(browser.find_element(By.XPATH, '//iframe[@id = "cyrinFrame"]'))
browser.find_element(By.XPATH, "//button[@id = 'computersMenuButton']").click()
time.sleep(3)
browser.find_element(By.XPATH, "//*[@id='displaymachine1_Ubuntu2004Desktop-4000-0182-eba4edce-809a-3fe20a37e1aa']").click()
time.sleep(4)

# switch to full screen
browser.find_element(By.XPATH, '//*[@id="btnToggleFullScreen"]').click()
time.sleep(2)

# Move to console icon and click it
action = ActionChains(browser)
action.move_to_element(browser.find_element(By.XPATH, "//*[@id = 'noVNC_screen']/div/canvas"))
time.sleep(2)
action.move_by_offset(-400, 390)
time.sleep(1)
action.click().perform()

time.sleep(10)



browser.switch_to.default_content()




# Code to end lab/exercise
browser.switch_to.frame(browser.find_element(By.XPATH, '//iframe[@id = "cyrinFrame"]'))
browser.find_element(By.XPATH, "//button[@id = 'btnEndExercise']").click()

time.sleep(2)
browser.find_element(By.XPATH, "//button[@id = 'btnConfirmEndExercise']").click()

time.sleep(10)