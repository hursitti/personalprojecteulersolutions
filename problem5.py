maxPrimeFactors = {}

def populatePrimeFactors(maxNum):
    x = 2
    while x < maxNum:
        prime = True
        for key in maxPrimeFactors.keys():
            if (x % key == 0):
                prime = False
                break
        if prime:
            maxPrimeFactors[x] = 0
        x += 1

populatePrimeFactors(20)

print (maxPrimeFactors)

