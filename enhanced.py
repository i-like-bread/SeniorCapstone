# Generated by Selenium IDE
import functions
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

"""
This script is generated from SeleniumIDE.
It  1) Launches the Getting Started Lab
    2) Switches to Computer A
    3) Opens the Terminal
    4) Enters "ls" in the Terminal (not showing?)
    5) Ends the Lab
"""

class TestCYRINTest():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_cYRINTest(self):
    # Test name: CYRINTest
    # Step # | name | target | value | comment
    # 1 | open | /mod/cyrin/view.php?id=166 |  | 
    userPrompt = functions.promptUser()
    print(userPrompt)
    self.driver.get("https://cyrin.atcorp.com/mod/cyrin/view.php?id=166")
    # 2 | setWindowSize | 1552x840 |  | 
    userPrompt = functions.promptUser()
    print(userPrompt)
    self.driver.set_window_size(1552, 840)
    # 3 | selectFrame | index=0 |  | 
    userPrompt = functions.promptUser()
    print(userPrompt)
    self.driver.switch_to.frame(0)
    # 4 | click | name=control |  | 
    userPrompt = functions.promptUser()
    print(userPrompt)
    self.driver.find_element(By.NAME, "control").click()
    # 5 | click | id=current-vm-name |  | 
    userPrompt = functions.promptUser()
    print(userPrompt)
    self.driver.find_element(By.ID, "current-vm-name").click()
    # 6 | click | id=machinestatus_Ubuntu2004Desktop-4000-0182-eba4edce-809a-3fe20a37e1aa |  | 
    userPrompt = functions.promptUser()
    print(userPrompt)
    self.driver.find_element(By.ID, "machinestatus_Ubuntu2004Desktop-4000-0182-eba4edce-809a-3fe20a37e1aa").click()
    # 7 | click | css=.exercise-page |  | 
    userPrompt = functions.promptUser()
    print(userPrompt)
    self.driver.find_element(By.CSS_SELECTOR, ".exercise-page").click()
    # 8 | click | css=#btnEndExercise > span:nth-child(1) |  | 
    userPrompt = functions.promptUser()
    print(userPrompt)
    self.driver.find_element(By.CSS_SELECTOR, "#btnEndExercise > span:nth-child(1)").click()
    # 9 | click | id=btnConfirmEndExercise |  | 
    userPrompt = functions.promptUser()
    print(userPrompt)
    self.driver.find_element(By.ID, "btnConfirmEndExercise").click()
