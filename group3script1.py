from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# import time
import os
import pytest

# For each line your read write it verbatim to the Enhanced Script file.
# If the line you read starts with # nn where nn is a number,
# write this line to the Enhanced Script file.
# Then write to the file the statement print(prompt_user()).
# Make sure the line you add is indented correctly.

# read the golden script
golden = open("isThisGolden.py", "r")

# the new script
outF = open("newScript.py", "w")

# Manually edit the Enhanced Script to add import team3module to top of script
outF.write("import group3script1")

# Read the Golden Script one line at a time.
for line in golden:
    outF.write(line)
    outF.write("\n")
    #if line.startswith('#'):
    #    outF.write("\n print(prompt_user()) \n")
    #else:
    #    outF.write(line)

outF.close()
golden.close()
