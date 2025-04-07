import time
import sys

def primeMultiplier (primes):
    reduced = 1
    unreduced = 0
    for x in primes:
        reduced *= x
    i = 1
    while i <= reduced:
        primish = True
        for x in primes:
            if (i % x == 0):
                primish = False
        if (primish):
            unreduced += 1
        i += 1
    return float(unreduced) / float(reduced)


#print("2")
#print(primeMultiplier([2]))
      
#print("2, 3")
#print(primeMultiplier([2, 3]))

#print("2, 3, 5")
#print(primeMultiplier([2, 3, 5]))

#print("2, 3, 5, 7")
#print(primeMultiplier([2, 3, 5, 7]))

#print("2, 3, 5, 7, 11")
#print(primeMultiplier([2, 3, 5, 7, 11]))

#print("2, 3, 5, 7, 11, 13")
#print(primeMultiplier([2, 3, 5, 7, 11, 13]))

def primishes (primes):
    product = 1
    ret = []
    for x in primes:
        product *= x
    i = product - 1
    while i > 0:
        primish = True
        for x in primes:
            if (i % x == 0):
                primish = False
        if (primish):
            ret.append(i)
        i -= 1
    return (product, ret)

#print (primishes([2, 3, 5, 7]))

def prime(primes, limit, x):
    if x > limit:
        return False
    for y in primes:
        if x % y == 0:
            return False
    return True

def sumOfPrimes(basePrimes, upto):
    primes = []
    p = primishes(basePrimes)
    step = p[0]
    subs = p[1]
    i = step
    end = upto + step
    total = long(0)
    total += sum(basePrimes)
    while i < end:
        for x in subs:
            possiblePrime = i - x
            if (possiblePrime != 1):
                if prime(primes, upto, possiblePrime):
                    primes.append(possiblePrime)
                    total += possiblePrime
        i += step
    return total

def runTrial(bp, upto):
    start = time.time()
    sop = sumOfPrimes(bp, upto)
    end = time.time()
    diff = end - start
    return (start, end, sop, diff)

def compareTrial(bp1, bp2, upto, trials):
    meanDiff1 = float(0)
    meanDiff2 = float(0)
    for x in range(0, trials):
        ret1 = runTrial(bp1, upto)
        ret2 = runTrial(bp2, upto)

        meanDiff1 += ret1[3]
        meanDiff2 += ret2[3]

        print bp1
        print ret1
        print bp2
        print ret2

    meanDiff1 /= trials
    meanDiff2 /= trials

    print("\nMean Difference for first base prime list: " + str(meanDiff1))
    print("Mean Difference for second base prime list: " + str(meanDiff2))


compareTrial([2], [2, 3, 5, 7, 11, 13], 2000000, 1)
































