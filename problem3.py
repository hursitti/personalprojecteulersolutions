listOfPrimes = []
includedPrimes = []

def inPrimeList (num):
    for x in listOfPrimes:
        if (x == num):
            return True
        if (num % x == 0):
            return False
    return True


def findPrimes (m):
    temp = m
    x = 2
    while (x < m):
        if inPrimeList(x):
            listOfPrimes.append(x)
            if (m % x == 0):
                includedPrimes.append(x)
                while (temp % x == 0):
                    temp = temp / x
        if (temp == 1):
            return
        x += 1

findPrimes(600851475143)
#print (listOfPrimes)
print (includedPrimes)
