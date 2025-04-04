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
    one = product - 1
    i = product
    while i > 0:
        primish = True
        for x in primes:
            if (i % x == 0):
                primish = False
        if (primish and i != one):
            ret.append(i)
        i -= 1
    return (product, ret)

print (primishes([2, 3, 5]))

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
    while i < end:
        for x in subs:
            possiblePrime = i - x
            if prime(primes, upto, possiblePrime):
                primes.append(possiblePrime)
        i += step
    print primes
    print (sum(primes) + sum(basePrimes))

sumOfPrimes([2, 3, 5, 7, 11], 1000)





































