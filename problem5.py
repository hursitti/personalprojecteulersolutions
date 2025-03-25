maxPrimeFactors = {}

def populatePrimeFactors(maxNum):
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

def numberPrimeFactors(num):
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

def uniqueSums(low, top):
    populatePrimeFactors(top)
    





