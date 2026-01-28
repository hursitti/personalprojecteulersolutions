import math

def pent(index):
    return int(index * ((index * 3) - 1)/2)

def intSqrt(n):
    t = math.sqrt(n)
    if (t == math.floor(t)):
        return int(t)
    return -1

def revPent(n):
    t = intSqrt(1 + (24*n))
    _t = 1 + t
    if (t == -1 or _t % 6 != 0):
        return -1
    return int(_t / 6)

def isPentNumber(n):
    return revPent(n) != -1

def generatePossibleBipents(topRange):
    ret = []
    for i in range(1, topRange):
        xi = pent(i)
        for j in range(1, i+1):
            xj = pent(j)
            ijSum = xi + xj
            ijDiff = xi - xj
            if (isPentNumber(ijSum) and isPentNumber(ijDiff)):
                ret.append((xi, xj))
    return ret


















