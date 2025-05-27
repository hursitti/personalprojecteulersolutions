import math
import time
import sys

def divisorNumber (number):
    x = 2
    total = 1
    while x <= number:
        if (number % x == 0):
            total += 1
        x += 1
    return total

def dn2 (number):
    x = 2
    total = 1
    remainder = number
    while x <= remainder:
        pNum = 0
        while(remainder % x == 0):
            pNum += 1
            remainder /= x
        total *= pNum + 1
        x += 1
    return total

def dn3 (number):
    x = 2
    total = 1
    remainder = number
    sq = math.sqrt(number)
    while x <= remainder and x < sq:
        pNum = 0
        while(remainder % x == 0):
            pNum += 1
            remainder /= x
        total *= pNum + 1
        x += 1
    if (total == 1):
        return 2
    return total


def findDivisorLength (number, dn):
    current, n = 3, 2
    while True:
        divisors = dn(current)
        if (divisors >= number):
            return (current, n)
        n += 1
        current += n

def compareTimes(number, trials, *funcs):
    x = 0
    for fn in funcs:
        deltaTimeAverage = 0
        for trial in range(trials):
            t = time.time()
            print (findDivisorLength(number, fn))
            deltaTimeAverage += time.time() - t
        print(x)
        print(deltaTimeAverage / trials)
        x += 1

compareTimes(150, 5, divisorNumber, dn2, dn3)
compareTimes(500, 10, dn2, dn3)
compareTimes(800, 5, dn2, dn3)
