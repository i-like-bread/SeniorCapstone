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
comment_pattern = '^\s*#\s*\d+\s+\|' # from start of line (^) look for zero
                                     # or more spaces (\s*) followed by #,
                                     # zero or more spaces, one or more digits,
                                     # zero or more spaces, and |

# Look for lines that match the comment_pattern.
# If a match is found, insert call to function prompt_user between this
# line and the next
cmd_to_insert = "user_action = prompt_user()"  # the command to be inserted
curr_line_num = 0  # current line number (start at top of file)
while lines[curr_line_num] != eof_line:
    curr_line = lines[curr_line_num]  # current line we are working with
    print(curr_line)
    # does line match Selenium comment line?
    match = re.match(comment_pattern, curr_line)
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

    # move to next line
    curr_line_num += 1 
        
# done inserting lines.  Write all lines to enhanced file
with open(enhanced_file_name, 'w') as ef:
    for i in range(0, len(lines)-1):
        ef.write(lines[i] + '\n')
