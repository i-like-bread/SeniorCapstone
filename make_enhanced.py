#!/usr/bin/python3

import re   # regular expressions

golden_file_name = "golden.py"
enhanced_file_name = "enhanced.py"

# Read golden file into memory as a list of lines
with open(golden_file_name, 'r') as gf:
    lines = gf.read().splitlines()

## Append a special end-of-file line to this list of lines
eof_line = "### End of file ###"
lines.append(eof_line)
        
# For each line in golden file that begins with "# number |", add below it
# a call to function prompt_user
comment_pattern = '^\s*#\s*\d+\s*\|\s*\w*\s*\|\s*css=canvas' # from start of line (^) look for zero
                                     # or more spaces (\s*) followed by #,
                                     # zero or more spaces, one or more digits,
                                     # zero or more spaces, |,
                                     # zero or more spaces, zero or more characters,
                                     # zero or more spaces, |,
                                     # zero or more spaces, and then "css=canvas
lab_start_button = '^\s*#\s*\d+\s*\|\s*\w*\s*\|\s*name=control' # regex to search for the line before the lab actually starts

computer_select_id = '    # 11 | click | id=computersMenuButton | ' # regex to search for the next action after the lab 
                                                                    # has been actually started

create_list = "user_responses = list()" # adds a line to create a list before the start of the ide code
lines.insert(15, create_list)

# Look for lines that match the comment_pattern.
# If a match is found, insert call to function prompt_user between this
# line and the next
cmd_to_insert = "user_responses.append((getframeinfo(currentframe()).lineno, functions.promptUser()))" # adds a tuple with the line number and the user response to the list
curr_line_num = 0  # current line number (start at top of file)
import_functions = "import functions" # added an import for the functions file
import_something = "from inspect import currentframe, getframeinfo" # Import for the file you suggested
lab_start_wait = 'WebDriverWait(self.driver, 45).until(expected_conditions.element_to_be_clickable((By.NAME, "control")))'
canvas_wait = 'WebDriverWait(self.driver, 180).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "canvas")))'
lines.insert(1, import_functions)  # inserted the import at the top of the enhanced file
lines.insert(1, import_something)
while lines[curr_line_num] != eof_line:
    curr_line = lines[curr_line_num]  # current line we are working with
    print(curr_line)
    # does line match Selenium comment line?
    match = re.match(comment_pattern, curr_line)
    lab_start = re.match(lab_start_button, curr_line)
    if match != None:
        # Found a Selenium comment.  Insert call to prompt_user after this line
        # Indentation of line to be added must match that of comment.
        num_spaces = len(curr_line) - len(curr_line.lstrip()) 

        # Form the line to write with num_spaces in front of the command to
        # insert.  To do this find the total length of the line to be inserted
        # (num of spaces + length of the command), and write the command to a
        # string with right justification
        total_line_len = num_spaces + len(cmd_to_insert)
        line_to_insert = cmd_to_insert.rjust(total_line_len, ' ')

        # insert line after current line
        lines.insert(curr_line_num+1, line_to_insert)
        curr_line_num += 1  # since we added one line
    elif lab_start != None:
        
        # Add a try: statement
        num_spaces = len(curr_line) - len(curr_line.lstrip())
        total_line_len = num_spaces + len("try:")
        line_to_insert = "try:".rjust(total_line_len, ' ')
        lines.insert(curr_line_num+1, line_to_insert)
        curr_line_num += 1
        
        # Adds a line that makes the script wait for the 'start lab' button to load
        new_line = "  " + lab_start_wait
        num_spaces = len(curr_line) - len(curr_line.lstrip())
        total_line_len = num_spaces + len(new_line)
        line_to_insert = (new_line).rjust(total_line_len, ' ')
        lines.insert(curr_line_num+1, line_to_insert)
        curr_line_num += 1
        
        # Add an 'except' statement
        new_line = "except Exception as e:"
        num_spaces = len(curr_line) - len(curr_line.lstrip())
        total_line_len = num_spaces + len(new_line)
        line_to_insert = (new_line).rjust(total_line_len, ' ')
        lines.insert(curr_line_num+1, line_to_insert)
        curr_line_num += 1
        
        # Print the exception
        new_line = "  print(e)"
        num_spaces = len(curr_line) - len(curr_line.lstrip())
        total_line_len = num_spaces + len(new_line)
        line_to_insert = (new_line).rjust(total_line_len, ' ')
        lines.insert(curr_line_num+1, line_to_insert)
        curr_line_num += 1
        
        # Quit script after printing exception
        new_line = "  self.driver.quit()"
        num_spaces = len(curr_line) - len(curr_line.lstrip())
        total_line_len = num_spaces + len(new_line)
        line_to_insert = (new_line).rjust(total_line_len, ' ')
        lines.insert(curr_line_num+1, line_to_insert)
        curr_line_num += 1

    # move to next line
    curr_line_num += 1 
        
# find name of the test class and test method created by Selenium
test_class_name = test_method_name = None
curr_line_num = 0
while test_class_name == None or test_method_name == None:
    if re.match("^\s*class\s+", lines[curr_line_num]) != None: 
        # Found line that starts with "class ". Get the second part of the line
        # which will have the name of the class
        test_class_name = lines[curr_line_num].split()[1]

        # Get rid of the "():" that is appended to the class name
        test_class_name = test_class_name.replace("():", "")
        print("Test class = ", test_class_name)

    if re.match("^\s*def\s*test_", lines[curr_line_num]) != None:
        # Found line that starts "def test_".  Get the second part of the line
        # which will have the name of the method
        test_method_name = lines[curr_line_num].split()[1]

        # Get rid of the "(self):" that is appended to the method name
        test_method_name = test_method_name.replace("(self):", "") 
        print("Test method = ", test_method_name)

    curr_line_num += 1

# inserts calls to run the enhanced file in memory, that are then written in the new enhanced file
lines.insert(len(lines)-1, "\ntestClass = " + test_class_name + "()")
lines.insert(len(lines)-1, 'testClass.setup_method("")')
lines.insert(len(lines)-1, "testClass." + test_method_name + "()")
lines.insert(len(lines)-1, 'testClass.teardown_method("")')
        
# done inserting lines.  Write all lines to enhanced file
with open(enhanced_file_name, 'w') as ef:
    for i in range(0, len(lines)-1):
        ef.write(lines[i] + '\n')