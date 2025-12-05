def simulateDivision(d):
    found = {} # (n, d) -> index
    n = 10
    result = "0."
    index = 2
    while (n % d != 0 and not((n, d) in found)):
        found[(n, d)] = index
        result = result + str(n//d)
        index += 1
        n = (n%d)*10

    if (n% d == 0):
        return result + str(n//d)
    else:
        startIndex = found[(n, d)]
        return result[0:startIndex] + "(" + result[startIndex:len(result)] + ")"

def getCycle(d):
    found = {} # (n, d) -> index
    n = 10
    result = "0."
    index = 2
    while (n % d != 0 and not((n, d) in found)):
        found[(n, d)] = index
        result = result + str(n//d)
        index += 1
        n = (n%d)*10

    if (n% d == 0):
        return 0
    else:
        startIndex = found[(n, d)]
        return index - startIndex

maxValue = 0
maxD = 2
for x in range(2, 1000):
    value = getCycle(x)
    print (str(x) + " " + str(value))
    if (value > maxValue):
        maxD = x
        maxValue = value
print ("max value: " + str(maxValue) + " at " + str(maxD)) 
