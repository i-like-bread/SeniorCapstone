from inspect import currentframe, getframeinfo
import functions

testList = list()

testList.append((getframeinfo(currentframe()).lineno, functions.promptUser()))
print(testList)

entry = testList[0]
item = entry[1]
print(item)

func = item[0]
print(func)

args = item[1]
print(args)