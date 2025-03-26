import math

def populatePrimeFactors(maxNum):
    maxPrimeFactors = {}
    x = 2
    while x < maxNum + 1:
        prime = True
        for key in maxPrimeFactors.keys():
            if (x % key == 0):
                prime = False
                break
        if prime:
            maxPrimeFactors[x] = 0
        x += 1
    return maxPrimeFactors

def numberPrimeFactors(num, maxPrimeFactors):
    factors = {}
    temp = num
    for x in maxPrimeFactors:
        while (temp % x == 0):
            if (factors.get(x) == None):
                factors[x] = 1
            else:
                factors[x] += 1
            temp /= x
    return factors

def uniqueFactors(low, top):
    mpf = populatePrimeFactors(top)
    for x in range(low, top + 1):
        pf = numberPrimeFactors(x, mpf)
        for (key, value) in pf.items():
            if mpf[key] == None or pf[key] > mpf[key]:
                mpf[key] = pf[key]
    return mpf

def sumOfFactors(pf):
    total = 1
    for (key, value) in pf.items():
        total *= math.pow(key, value)
    return total

print(sumOfFactors(uniqueFactors(2, 20)))





