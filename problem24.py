import math
import time

def simplePermutation (currString, charSet):
    retSet = set()
    for c in charSet:
        retSet.update(simplePermutation(currString + c, charSet - {c}))
    if len(charSet) == 0:
        return {currString}
    return retSet

def getOrderedPermutation (index, orderedList, currString):
    length = len(orderedList)
    if (length == 1):
        return currString + orderedList[0]
    fact = math.factorial(length)
    nextFact = int(fact / length)
    headCharIndex = int(index/nextFact)
    headChar = orderedList[headCharIndex]
    return getOrderedPermutation(index % nextFact, [x for x in orderedList if x != headChar], currString + headChar)

print(time.time())
print(getOrderedPermutation (999999, ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], ""))
print(time.time())
