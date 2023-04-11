#!/usr/bin/python3
# Beep Bop
from textwrap import dedent # to dedent the new code for test_script.py
import sys
import re   # regular expressions
from make_enhanced_utils import make_wait_command

golden_file_name = "Test_Script.py"
enhanced_file_name = "test_file.py"

# Read golden file into memory as a list of lines
with open(golden_file_name, 'r') as gf:
    lines = gf.read().splitlines()



# Add explicit wait before click of button confirming ending of lab
confirm_end_btn_pattern = '^\s*self\.driver\.find_element\(By.ID, "btnConfirmEndExercise"\)'
cmd_to_insert = make_wait_command(120, 'By.ID, "btnConfirmEndExercise"')
for line_num, line in enumerate(lines):
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
            lines.insert(line_num+num_lines_inserted, line_to_insert)
            num_lines_inserted += 1
        break
    

## Add call to function.prompt_user before any action on canvas
canvas_action_pattern = '^\s*\w+\s*=\s*self\.driver\.find_element\(By\.CSS_SELECTOR, "canvas"\)'
cmd_to_insert = "user_responses.append((getframeinfo(currentframe()).lineno, functions.promptUser()))" # adds a tuple with the line number and the user response to the list
line_num = 0 # current line number in lines being processed
while line_num < len(lines):
    match = re.match(canvas_action_pattern, lines[line_num])
    if match != None:
        # found line with action on canvas.  Insert call to prompt_user after
        # this line

        # find indentation of current line (num spaces)
        num_spaces = len(line) - len(line.lstrip()) 

        # add necessary number of spaces before cmd_to_insert 
        total_line_len = num_spaces + len(cmd_to_insert)
        line_to_insert = cmd_to_insert.rjust(total_line_len, ' ')

        # insert line before current line and increment line_num
        lines.insert(line_num, line_to_insert)
        line_num += 1  # since we added a line
    if line_num == 20+1:
        lines.insert(line_num, "PLEASE WORK")
        lines.pop(line_num-1)
    line_num += 1  # go to next line

# add code to create test_script after everything else
curr_line_num = len(lines)+1

# Writing the code to create test_script.py in a multi-lined String
test_script_code = dedent("""
    current_file = 'enhanced.py'
    new_file = 'test_script.py'
    
    with open(current_file, 'r') as gf:
       lines = gf.read().splitlines()
       
    prompt_user_pattern = "^\s*user_responses\.append\(\(getframeinfo\(currentframe\(\)\)\.lineno, functions\.prompt_user\(\)\)\)" 
    line_num = 0
    for line_num, line in enumerate(lines):
        while line_num < len(lines):
            # Check for a line that contains prompt_user
            match = re.match(prompt_user_pattern, lines[line_num])
            if match != None:
                for item_num, item in enumerate(user_responses):
                    # Check to make sure that the current line matches with a line from user_responses
                    if line_num == user_responses[item_num][0]:
                        line.replace(line, 'perform_action(' + user_responses[item_num][1] + ')')
    """)

# Add the new code for the test_script to the file in memory
lines.insert((curr_line_num), test_script_code)

# done inserting lines.  Write all lines to enhanced file
with open(enhanced_file_name, 'w') as ef:
    for line_num, line in enumerate(lines):
        ef.write(line + '\n')

sys.exit("Created file " + enhanced_file_name)

# for each action collected in list user_responses:
#   * go to line number of response (that line will have the call to prompt_user
#   * replace line with perform_action(ACTION_FROM_USER_RESPONSES)
#   * write contents of line array to file test_script.py