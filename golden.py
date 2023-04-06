# Generated by Selenium IDE
import pytest
import time
import json
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

class TestGolden3():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_golden3(self):
    # Test name: golden3
    # Step # | name | target | value
    # 1 | open | /login/index.php | 
    self.driver.get("https://cyrin.atcorp.com/course/view.php?id=37")
    # 2 | setWindowSize | 1552x840 | 
    self.driver.set_window_size(1552, 840)
    # 3 | click | id=username | 
    self.driver.find_element(By.ID, "username").click()
    # 4 | type | id=username |
    self.driver.find_element(By.ID, "username").send_keys(username)
    # 5 | click | id=password | 
    self.driver.find_element(By.ID, "password").click()
    # 6 | type | id=password | 
    self.driver.find_element(By.ID, "password").send_keys(password)
    # 7 | click | id=loginbtn | 
    self.driver.find_element(By.ID, "loginbtn").click()
    # 8 | click | css=.activity-btn:nth-child(1) | 
    self.driver.find_element(By.CSS_SELECTOR, ".activity-btn:nth-child(1)").click()
    # 9 | selectFrame | index=0 | 
    self.driver.switch_to.frame(0)
    # 10 | click | name=control | 
    self.driver.find_element(By.NAME, "control").click()
    # 11 | click | css=.no-fullscreen:nth-child(1) | 
    self.driver.find_element(By.CSS_SELECTOR, ".no-fullscreen:nth-child(1)").click()
    # 12 | click | id=computersMenuButton | 
    self.driver.find_element(By.ID, "computersMenuButton").click()
    # 13 | click | id=machinestatus_Ubuntu2004Desktop-4000-0182-eba4edce-809a-3fe20a37e1aa | 
    self.driver.find_element(By.ID, "machinestatus_Ubuntu2004Desktop-4000-0182-eba4edce-809a-3fe20a37e1aa").click()
    # 14 | mouseDown | css=canvas | 
    element = self.driver.find_element(By.CSS_SELECTOR, "canvas")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 15 | mouseUp | id=noVNC_mouse_capture_elem | 
    element = self.driver.find_element(By.ID, "noVNC_mouse_capture_elem")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    # 16 | click | css=.exercise-page | 
    self.driver.find_element(By.CSS_SELECTOR, ".exercise-page").click()
    # 17 | mouseDown | css=canvas | 
    element = self.driver.find_element(By.CSS_SELECTOR, "canvas")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 18 | mouseUp | id=noVNC_mouse_capture_elem | 
    element = self.driver.find_element(By.ID, "noVNC_mouse_capture_elem")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    # 19 | click | css=.exercise-page | 
    self.driver.find_element(By.CSS_SELECTOR, ".exercise-page").click()
    # 20 | mouseDown | css=canvas | 
    element = self.driver.find_element(By.CSS_SELECTOR, "canvas")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    # 21 | mouseUp | id=noVNC_mouse_capture_elem | 
    element = self.driver.find_element(By.ID, "noVNC_mouse_capture_elem")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    # 22 | click | css=.exercise-page | 
    self.driver.find_element(By.CSS_SELECTOR, ".exercise-page").click()
    # 23 | click | id=btnEndExercise | 
    self.driver.find_element(By.ID, "btnEndExercise").click()
    # 24 | click | id=btnConfirmEndExercise | 
    self.driver.find_element(By.ID, "btnConfirmEndExercise").click()