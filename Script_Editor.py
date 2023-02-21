""" A function that loops through the Golden_Script.py file and adds in 
calls to the selenMod.py function before each line of code."""
import re

def scriptEnhancer():
    regex = "^\s+#\s\d+"
    file = open("Enhanced_Script.py", "w")
    file.write("import selenMod\n")
    with open("Golden_Script.py") as script:
        for line in script:
            if re.match(regex, line):
                file.write("    self.driver.pick_option()\n")
                file.write(line)
                file.write("\n")
            else:
                file.write(line)

    
scriptEnhancer()