# Generated by Selenium IDE
import pytest
import time
import json
import functions
from inspect import currentframe, getframeinfo
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from getpass import getpass

username = input("Enter Username: ")
password = getpass()

user_responses = list()  # list of user specified actions

class TestTestrecon():
  def setup_method(self, method):
    self.chrome_options = webdriver.ChromeOptions()
    self.chrome_options.add_argument('--no-sandbox')
    self.driver = webdriver.Chrome(options=self.chrome_options)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testrecon(self):
    # Test name: test-recon
    # Step # | name | target | value
    # 1 | open | /login/index.php | 
    self.driver.get("https://cyrin.atcorp.com/mod/cyrin/view.php?id=33")
    # 2 | setWindowSize | 1920x1055 | 
    self.driver.set_window_size(1920, 1055)
    # 3 | type | id=username | username
    self.driver.find_element(By.ID, "username").send_keys(username)
    # 4 | type | id=password | password
    self.driver.find_element(By.ID, "password").send_keys(password)
    # 5 | click | id=loginbtn | 
    self.driver.find_element(By.ID, "loginbtn").click()
    # 6 | selectFrame | index=0 | 
    self.driver.switch_to.frame(0)
    # 7 | click | name=control | 
    try:
        wait = WebDriverWait(self.driver, 120)
        wait.until(expected_conditions.element_to_be_clickable((By.NAME, "control")))
    except:
        print('By.NAME, "control" did not become clickable')
        self.driver.quit()
    self.driver.find_element(By.NAME, "control").click()
    try:
        wait = WebDriverWait(self.driver, 360)
        wait.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "canvas")))
    except:
        print('By.CSS_SELECTOR, "canvas" did not become clickable')
        self.driver.quit()
    # 8 | mouseDown | css=canvas | 
    functions.perform_action(('MouseClick', (168, 836)))
    element = self.driver.find_element(By.CSS_SELECTOR, "canvas")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 9 | mouseUp | id=noVNC_mouse_capture_elem | 
    element = self.driver.find_element(By.ID, "noVNC_mouse_capture_elem")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    # 10 | click | css=.exercise-page | 
    self.driver.find_element(By.CSS_SELECTOR, ".exercise-page").click()
    # 11 | mouseDown | css=canvas | 
    functions.perform_action(('MouseClick', (176, 486)))
    element = self.driver.find_element(By.CSS_SELECTOR, "canvas")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 12 | mouseUp | id=noVNC_mouse_capture_elem | 
    element = self.driver.find_element(By.ID, "noVNC_mouse_capture_elem")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    # 13 | click | css=.exercise-page | 
    self.driver.find_element(By.CSS_SELECTOR, ".exercise-page").click()
  

testClass = TestTestrecon()
testClass.setup_method("")
testClass.test_testrecon()
print("Sleeping for 30 seconds. End lab manually and log out if you want")
time.sleep(30)
testClass.teardown_method("")

