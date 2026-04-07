def cutoffPow (x, n):
    i = 0
    ret = 1
    while i < n:
        ret = (ret * x) % 10000000000
        i += 1
    return ret

def cutoffSum(xList):
    total = 0
    for x in xList:
        total = (total + x) % 10000000000
    return total

xList = [cutoffPow(x, x) for x in range(1, 1001)]
print (cutoffSum(xList))