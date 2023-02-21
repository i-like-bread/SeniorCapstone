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
                file.write("    self.driver.pick_option()\n")
                file.write(line)
            # else, the line is just written to the new file
            else:
                file.write(line)

    
scriptEnhancer()