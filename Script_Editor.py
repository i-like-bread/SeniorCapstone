""" A function that loops through the Golden_Script.py file and adds in 
calls to the selenMod.py function before each line of code."""
import re

def scriptEnhancer():
    regex = "^\s+#\s\d+"                    # regex to match any comment that is tabbed in and starts with a number
    file = open("Enhanced_Script.py", "w")  # Create a new file for the Enhanced_Script
    file.write("import selenMod\n")         # Write the import to the Team2 module at the beginning of the script
    
    # Opens the Golden_Script.py and loops through it
    with open("Golden_Script.py") as script:
        for line in script:
            
            # if the line is a tabbed in comment that starts with a number, then the Team2 function is called
            if re.match(regex, line):
                file.write("\n")
                file.write("    # Prompts the user for next action\n")
                file.write("    selenMod.pick_option()\n")
                file.write(line)
                
            # else, the line is just written to the new file
            else:
                file.write(line)
                
    # Insert calls at the end of the Enhanced_Script.py to actually run the new script
    file.write("\n\n# Running the functions to run the test\n")
    file.write("testClass = TestCYRINTest()\n\n")
    file.write('testClass.setup_method("")\n')
    file.write("testClass.test_cYRINTest()\n")
    file.write('testClass.teardown_method("")')
    
# Runs the function and creates Enhanced_Script.py
scriptEnhancer()