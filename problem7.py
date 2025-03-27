primeList = []

def isPrime(x):
    for y in primeList:
        if (x % y == 0):
            return False
    return True

def populateUptoPrime(num):
    i = 0
    x = 2
    while i < num:
        if (isPrime(x)):
            i += 1
            primeList.append(x)
        x += 1
        
populateUptoPrime(10001)
print(primeList[10000])
