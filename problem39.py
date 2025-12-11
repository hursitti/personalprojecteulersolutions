
primeSet = set()

def buildPrimeSet(n, pSet):
    i = 2
    while (i < n):
        prime = True
        for p in pSet:
            if (i % p == 0):
                prime = False
                break
        if (prime):
            pSet.add(i)
        i += 1

buildPrimeSet(1001, primeSet)

def factorCount (x, p):
    ret = 0
    while (x % p == 0):
        ret += 1
        x = x / p
    return ret

def intSqrt (x, pSet):
    if (x == 1):
        return x
    ret = x
    for p in pSet:
        count = factorCount(x, p)
        if (count % 2 != 0):
            return -1
        elif (count > 0):
            ret = ret / (p**(count/2))
    return ret

def checkPerimeter(per):
    ret = set()
    a = int(per // 2)
    lim = int(per // 3) - 1
    while (a > lim):
        b = int((per - a) // 2)
        while (b > 0):
            c = intSqrt((a*a)+(b*b), primeSet)
            if (per == a + b + c):
                ret.add((a, b, c))
            b -= 1
        a -= 1
    return ret

def rtAtPerimeter(per):
    ret = 0
    a = int(per // 2)
    lim = int(per // 3) - 1
    while (a > lim):
        b = int((per - a) // 2)
        while (b > 0):
            c = intSqrt((a*a)+(b*b), primeSet)
            if (per == a + b + c):
                ret += 1
            b -= 1
        a -= 1
    return ret

def mostRTUpto(upto):
    p = 1
    maxRTIndex = 1
    maxRTs = 0
    while (p < upto):
        t = rtAtPerimeter(p)
        print ("{_t} at {_p}".format(_t = t, _p = p))
        if (t > maxRTs):
            maxRTIndex = p
            maxRTs = t
        p += 1
    return maxRTIndex



























