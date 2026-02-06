import math

def intSqrt(n):
    t = math.sqrt(n)
    if (t == math.floor(t)):
        return int(t)
    return -1

#k = 1
def getYfromXandD(x, d):
    ret = intSqrt((float((x*x) - 1))/float(d))
    if (ret < 1):
        return -1
    return ret

#k = 1
def naivePellSearch(upto):
    ret = []
    for d in range(2, upto+1):
        if (intSqrt(d) != -1):
            continue
        x = 1
        found = False
        while not found:
            y = getYfromXandD(x, d)
            if (y > 0):
                ret.append((x, y, d))
                found = True
                print(repr((x, y, d)))
            x += 1
    return ret

# based on https://en.wikipedia.org/wiki/Chakravala_method
# and studying the implementation here: https://www.jakebakermaths.org.uk/maths/jshtmlpellsolverbigintegerv10.html
def getLowestM (a, b, k, n, choosePositive=True):
    currM = 1
    greaterThanMFound = False
    retM = []
    absK = abs(k)
    while not greaterThanMFound:
        currMSquared = currM * currM
        if ((a + (b*currM)) % absK == 0 and ((not choosePositive) or currMSquared >= n)):
            retM.append((currM, abs((currMSquared)-n)))
            if (currMSquared >= n):
                greaterThanMFound = True
        currM += 1
    return min(retM, key = lambda tup : tup[1])[0]
def getTripletFromM(m, _a, _b, _k, n):
    a = ((_a*m) + (n*_b))/abs(_k)
    b = (_a + (_b*m))/abs(_k)
    k = ((m*m) - n)/_k
    return (a, b, k)
def startingTriple(n):
    b = 1
    a = 1
    while a*a < n:
        a += 1
    k = ((a*a) - n)
    return (a, b, k)
def chakravala(d, k, choosePositive=True):
    latest = startingTriple(d)
    step = 0
    while (latest[2] != k):
        latest = getTripletFromM(getLowestM(latest[0], latest[1], latest[2], d, choosePositive), latest[0], latest[1], latest[2], d)
    return latest

def chakravalaList(d, k, choosePositive=True, maxSteps=-1):
    ret = [startingTriple(d)]
    latest = ret[0]
    step = 0
    while (latest[2] != k and (step < maxSteps or maxSteps == -1)):
        latest = getTripletFromM(getLowestM(latest[0], latest[1], latest[2], d, choosePositive), latest[0], latest[1], latest[2], d)
        ret.append(latest)
        step += 1
    return ret

def chakravalaSearch(upto):
    maxX = ((-1, -1, -1), -1)
    for d in range(1, upto+1):
        if (intSqrt(d) != -1):
            continue
        res = chakravala(d, 1)
        if (res[0] > maxX[0][0]):
            maxX = (res, d)
    return maxX


























            
