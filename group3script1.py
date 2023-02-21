import re

# read the golden script
golden = open("isThisGolden.py", "r")

# the new script
outF = open("newScript.py", "a")

# Manually edit the Enhanced Script to add import team3module to top of script
outF.write("import selenMod \n")

regex = r"\s+#"

# Read the Golden Script one line at a time.
for line in golden:
    # If the line you read starts with # nn where nn is a number,
    # write this line to the Enhanced Script file.
    # Then write to the file the statement print(prompt_user()).
    if re.match(regex, line):
        outF.write(line)
        outF.write("\n    selenMod.pick_option() \n")
    else:
        # For each line your read write it verbatim to the Enhanced Script file.
        outF.write(line)
    outF.write("\n")

outF.close()
golden.close()
