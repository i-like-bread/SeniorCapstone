# Generated by Selenium IDE
import pytest
import time
import json
import sys
import re
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
    # 11 | click | css=.no-fullscreen:nth-child(1) | 
    self.driver.find_element(By.CSS_SELECTOR, ".no-fullscreen:nth-child(1)").click()
    # 12 | click | id=computersMenuButton | 
    self.driver.find_element(By.ID, "computersMenuButton").click()
    # 13 | click | id=machinestatus_Ubuntu2004Desktop-4000-0182-eba4edce-809a-3fe20a37e1aa | 
    self.driver.find_element(By.ID, "machinestatus_Ubuntu2004Desktop-4000-0182-eba4edce-809a-3fe20a37e1aa").click()
    # 14 | mouseDown | css=canvas | 
    user_responses.append((getframeinfo(currentframe()).lineno, functions.promptUser()))
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
    user_responses.append((getframeinfo(currentframe()).lineno, functions.promptUser()))
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
    user_responses.append((getframeinfo(currentframe()).lineno, functions.promptUser()))
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
    try:
        wait = WebDriverWait(self.driver, 120)
        wait.until(expected_conditions.element_to_be_clickable((By.ID, "btnConfirmEndExercise")))
    except:
        print('By.ID, "btnConfirmEndExercise" did not become clickable')
        self.driver.quit()
    self.driver.find_element(By.ID, "btnConfirmEndExercise").click()

testClass = TestGolden3()
testClass.setup_method("")
testClass.test_golden3()
testClass.teardown_method("")

current_file = 'enhanced.py'
new_file = 'test_script.py'

with open(current_file, 'r') as gf:
  lines = gf.read().splitlines()

prompt_user_pattern = "^\s*user_responses\.append\(\(getframeinfo\(currentframe\(\)\)\.lineno, functions\.promptUser\(\)\)\)" 
line_num = 0
for line_num, line in enumerate(lines):
  while line_num < len(lines):
    # Check for a line that contains prompt_user
    match = re.match(prompt_user_pattern, lines[line_num])
    if match != None:
      for item_num, item in enumerate(user_responses):
        # Check to make sure that the current line matches with a line from user_responses
        if (line_num+1) == user_responses[item_num][0]:
          args = user_responses[item_num][1]
          action = args[0]
          action = '"' + action + '"'
          arg1 = ""
          arg2 = ""
          match action:
            case "noop":
              arg1 = "()"
            case "Wait":
              arg1 = ''.join(map(str, args[1]))
            case "KeyboardInput":
              arg1 = args[1]
            case "MouseClick":
              action_args = args[1]
              x_coord = action_args[0]
              y_coord = action_args[1]
              arg1 = str(x_coord)
              arg2 = str(y_coord)
              arg1 = arg1 + ", " + arg2
          lines.insert(line_num, '    functions.performAction((' + action + ', (' + arg1 + ')))')
          lines.pop(line_num+1)
      break        
    else:
      line_num += 1

with open(new_file, 'w') as ef:
    for line_num, line in enumerate(lines):
        ef.write(line + "\n")

sys.exit("Created file " + new_file)

