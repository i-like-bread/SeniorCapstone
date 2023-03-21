from inspect import currentframe, getframeinfo
import functions

testList = list()

testList.append((getframeinfo(currentframe()).lineno, functions.promptUser()))
print(testList)