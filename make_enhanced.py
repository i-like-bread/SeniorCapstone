#!/usr/bin/python3

import sys
import re   # regular expressions
from make_enhanced_utils import make_wait_command

golden_file_name = "golden.py"
enhanced_file_name = "enhanced.py"
test_file_name = "test.py"

# Read golden file into a list of lines call escript (enhanced
# script).  The escript is an enhanced version of the golden script
with open(golden_file_name, 'r') as gf:
    escript = gf.read().splitlines()

## Add the imports we need
# look for the first line that starts with "from selenium" and add our imports
# before the selenium imports
import_inspect = "from inspect import currentframe, getframeinfo"
import_our_functions = "import functions"
import_pattern = "^from\s+selenium"
import_found = False
for line_num, line in enumerate(escript):
    match = re.match(import_pattern, escript[line_num])
    if match != None:
        # found line that imports from selenium. Insert our imports above
        # this line and break out of loop
        escript.insert(line_num, import_inspect)
        escript.insert(line_num, import_our_functions)
        import_found = True
        break
if import_found == False:
    sys.exit("Failed to add necessary imports")


# Insert declaration for list user_responses just before definition of
# test class generated by Selenium.
line_to_insert = "user_responses = list()  # list of user specified actions"
class_def_pattern = "^class\s+"
class_def_found = False
for line_num, line in enumerate(escript):
    match = re.match(class_def_pattern, line)
    if match != None:
        # found line with class definition.  Insert declaration and break
        # out of loop
        escript.insert(line_num, "")
        escript.insert(line_num, line_to_insert)
        class_def_found = True
        break
if class_def_found == False:
    sys.exit("Failed to add declaration for list user_responses")


# Insert lines required to set Chrome options just before webdriver is created.
# Also replace webdriver creation line with one that includes Chrome options.
# These options are needed since we will be running Chrome as root user.  Need
# to run as root on Linux because of package keyboard.
lines_to_insert = []
lines_to_insert.append("self.chrome_options = webdriver.ChromeOptions()")
lines_to_insert.append("self.chrome_options.add_argument('--no-sandbox')")
lines_to_insert.append("self.driver = webdriver.Chrome(options=self.chrome_options)")
driver_create_pattern = '\s*self.driver\s*=\s*webdriver.Chrome'
for line_num, line in enumerate(escript):
    match = re.match(driver_create_pattern, line)
    if match != None:
        # found line that creates web driver
        # find indentation of current line (num spaces)
        num_spaces = len(line) - len(line.lstrip()) 

        # delete original create webdriver (line we found)
        del escript[line_num]

        # indent and insert new lines 
        for i, line in enumerate(lines_to_insert):
            total_line_len = num_spaces + len(line)
            line_to_insert = line.rjust(total_line_len, ' ')
            escript.insert(line_num+i, line_to_insert)

        break  # all done 
    
## Add a line to set the window position of the browser to 0 x 0
# Also inserts a comment that mimics ones from Selenium IDE
lines_to_insert = []
lines_to_insert.append("# 2 | setWindowPosition | 0X0 |")
lines_to_insert.append("self.driver.set_window_position(0, 0)")
window_size_pattern = '\s*self\.driver\.set_window_size'
for line_num, line in enumerate(escript):
    match = re.match(window_size_pattern, line)
    if match != None:
        # found line that sets the window size
        # find indentation of current line (num spaces)
        num_spaces = len(line) - len(line.lstrip())
        
        #indent and insert new lines
        for i, line in enumerate(lines_to_insert):
            total_line_len = num_spaces + len(line)
            line_to_insert = line.rjust(total_line_len, ' ')
            escript.insert(line_num+i, line_to_insert)
            
        break # all done
        
## Add explicit waits for certain HTML elements to be loaded (e.g. start
## button, canvas, etc)
# To add an explicit wait, call function make_wait_command with max time to
# wait and how the element is found by Selenium (e.g. By.NAME).
# The return value will a list of strings, where each string is a line to be
# inserted into the enhanced script
# Add explicit wait for start button (By.name, "control").
control_btn_pattern = '\s*self\.driver\.find_element\(By.NAME, "control"\)'
cmd_to_insert = make_wait_command(120, 'By.NAME, "control"') 
for line_num, line in enumerate(escript):
    match = re.match(control_btn_pattern, line)
    if match != None:
        # found line that clicks control button.  Insert wait for button to be
        # clickable and exit
        
        # find indentation of current line (num spaces)
        num_spaces = len(line) - len(line.lstrip()) 

        # Form the line to write with num_spaces in front of the command to
        # insert.  To do this find the total length of the line to be inserted
        # (num of spaces + length of the command), and write the command to a
        # string with right justification
        num_lines_inserted = 0
        for l in cmd_to_insert:
            total_line_len = num_spaces + len(l)
            line_to_insert = l.rjust(total_line_len, ' ')

            # insert line after current line
            escript.insert(line_num+num_lines_inserted, line_to_insert)
            num_lines_inserted += 1
        break

# Add explicit wait for canvas to be ready AFTER start ("control") button
# is clicked
control_btn_pattern = '\s*self\.driver\.find_element\(By.NAME, "control"\)'
cmd_to_insert = make_wait_command(360, 'By.CSS_SELECTOR, "canvas"')
for line_num, line in enumerate(escript):
    match = re.match(control_btn_pattern, line)
    if match != None:
        # found line that clicks control button.  Insert wait for canvas 
        # to load after control button is clicked.

        # find indentation of current line (num spaces)
        num_spaces = len(line) - len(line.lstrip()) 

        # Form the line to write with num_spaces in front of the command to
        # to insert
        num_lines_inserted = 0
        for l in cmd_to_insert:
            total_line_len = num_spaces + len(l)
            line_to_insert = l.rjust(total_line_len, ' ')

            # insert line after current line
            escript.insert(line_num+num_lines_inserted+1, line_to_insert)
            num_lines_inserted += 1
        break

# Add explicit wait before click of button confirming ending of lab
confirm_end_btn_pattern = '^\s*self\.driver\.find_element\(By.ID, "btnConfirmEndExercise"\)'
cmd_to_insert = make_wait_command(120, 'By.ID, "btnConfirmEndExercise"')
for line_num, line in enumerate(escript):
    match = re.match(confirm_end_btn_pattern, line)
    if match != None:
        # found line that clicks button to confirm ending lab.
        # Insert wait for button to load

        # find indentation of current line (num spaces)
        num_spaces = len(line) - len(line.lstrip()) 

        # Form the line to write with num_spaces in front of the command to
        # to insert
        num_lines_inserted = 0
        for l in cmd_to_insert:
            total_line_len = num_spaces + len(l)
            line_to_insert = l.rjust(total_line_len, ' ')

            # insert line after current line
            escript.insert(line_num+num_lines_inserted, line_to_insert)
            num_lines_inserted += 1
        break
    

## Add call to function.prompt_user before any action on canvas
canvas_action_pattern = '^\s*\w+\s*=\s*self\.driver\.find_element\(By\.CSS_SELECTOR, "canvas"\)'
# The command to insert is a call to prompt_user.  The line number from which
# this call is made and the return value of prompt_user are stored in
# list user_responses.  We store lineno-1 because line 1 is escript[0], etc.
cmd_to_insert = "user_responses.append((getframeinfo(currentframe()).lineno-1, functions.prompt_user()))"
line_num = 0 # current line number in escript being processed
while line_num < len(escript):
    match = re.match(canvas_action_pattern, escript[line_num])
    if match != None:
        # found line with action on canvas.  Insert call to prompt_user after
        # this line
        line = escript[line_num]

        # find indentation of current line (num spaces)
        num_spaces = len(line) - len(line.lstrip()) 

        # add necessary number of spaces before cmd_to_insert 
        total_line_len = num_spaces + len(cmd_to_insert)
        line_to_insert = cmd_to_insert.rjust(total_line_len, ' ')

        # insert line before current line and increment line_num
        escript.insert(line_num, line_to_insert)
        line_num += 1  # since we added a line
    line_num += 1  # go to next line
    
## find name of the test class and test method created by Selenium
test_class_name = test_method_name = None
curr_line_num = 0
while test_class_name == None or test_method_name == None:
    if re.match("^\s*class\s+", escript[curr_line_num]) != None: 
        # Found line that starts with "class ". Get the second part of the line
        # which will have the name of the class
        test_class_name = escript[curr_line_num].split()[1]

        # Get rid of the "():" that is appended to the class name
        test_class_name = test_class_name.replace("():", "")

    if re.match("^\s*def\s*test_", escript[curr_line_num]) != None:
        # Found line that starts "def test_".  Get the second part of the line
        # which will have the name of the method
        test_method_name = escript[curr_line_num].split()[1]

        # Get rid of the "(self):" that is appended to the method name
        test_method_name = test_method_name.replace("(self):", "") 

    curr_line_num += 1

# find end exercise button click and replace with a new line that will actually close it
for line_num, line in enumerate(escript):
    if re.match("^\s*self.driver.find_element(By.ID, 'btnEndExercise').click()", line):
        escript.replace("self.driver.find_element(By.ID, 'btnEndExercise').click()", "self.driver.execute_script('document.getElementById('btnEndExercise').click()')")

# inserts calls to create test class and to run test
escript.append("")   # blank line for readability
escript.append("testClass = " + test_class_name + "()")
escript.append('testClass.setup_method("")')
escript.append("testClass." + test_method_name + "()")
escript.append('print("Sleeping for 30 seconds. End lab manually and log out if you want")')
escript.append('time.sleep(30)')
escript.append('testClass.teardown_method("")')
        
## Replace calls to prompt_user with calls of perform_action in array escript.
# When the enhanced script gets to this point, the list user_responses
# already has in it line numbers and responses from prompt_user
marker_line = "### THE FOLLOWING LINES SHOULD NOT APPEAR IN TEST SCRIPT ###"
escript.append("")   # blank line for readability
escript.append(marker_line)
escript.append("## Create test script by modifying the in-memory enhanced script")
# for each entry in user_responses, find lines where prompt_user is to be
# replaced by perform_action, and do the replacement
escript.append("for _, user_resp in enumerate(user_responses):")
escript.append("    line_num = user_resp[0]")
escript.append("    action = user_resp[1]")
escript.append("    curr_line = escript[line_num]  # current line at line_num") 
escript.append("    replacement_line = f'functions.perform_action({action})'")
escript.append("    # find indentation of current line")
escript.append("    num_spaces = len(curr_line) - len(curr_line.lstrip())")
escript.append("    total_line_len = num_spaces + len(replacement_line)")
escript.append("    indented_replacement = replacement_line.rjust(total_line_len, ' ')")
escript.append("    print(f'Replacing {line_num}: {curr_line} with {indented_replacement}')") 
escript.append("    # replace prompt_user line with perform_action line")
escript.append("    escript[line_num] = indented_replacement")
    
# write lines to enhanced script that will create the test script 
escript.append("")   # blank line for readability
escript.append("# Write to test script file")
escript.append(f'test_file_name = "{test_file_name}"')
escript.append("with open(test_file_name, 'w') as tf:")
escript.append("    for _, line in enumerate(escript):")
escript.append("        if line != marker_line:")
escript.append("            tf.write(line + '\\n')")
escript.append("        else:")
escript.append("            break")

# done creating escript.  Write it to enhanced file.  We are writing to
# this file for debugging purposes only.  It is not required otherwise.
with open(enhanced_file_name, 'w') as ef:
    for _, line in enumerate(escript):
        ef.write(line + '\n')
             
# Convert the array of strings in escript to a multi-line string that we will
# execute. Form this multi-line string by joining all the lines in the list
# escript into a single string with a newline between them
str_to_execute = "\n".join( line for line in escript)

# execute this string.  Pass in the array escript to this script.  This is so
# the script can replace the escript in lin
exec(str_to_execute, {'escript':escript, 'marker_line':marker_line})

sys.exit(f'Completed exection of {__file__}')

