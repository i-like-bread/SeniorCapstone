from inspect import currentframe, getframeinfo
import functions
import re

# testList = list()

# testList.append((getframeinfo(currentframe()).lineno, functions.promptUser()))
# print(testList)

# entry = testList[0]
# item = entry[1]
# print(item)

# func = item[0]
# print(func)

# args = item[1]
# print(args)

comment_pattern = "^\s*user_responses\.append\(\(getframeinfo\(currentframe\(\)\)\.lineno, functions\.promptUser\(\)\)\)"

match = re.match(comment_pattern, "     user_responses.append((getframeinfo(currentframe()).lineno, functions.promptUser()))")

if match != None:
    print("Hell yeah!")
else:
    print("Dammit")