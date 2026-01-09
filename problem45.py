import math

def calcT(t):
    return t*(t+1)/2

def calcP(p):
    return p*(3*p-1)/2

def calcH(h):
    return h*(2*h-1)

#a modified version of https://en.wikipedia.org/wiki/Square_root_algorithms#Heron's_method to get a real number root if it exists
def intHeron(n):
    n = float(n)
    diff = 1.0
    t = n/2
    while (diff > 0.1):
        _t = (t + (n/t))/2
        diff = t - _t
        #print((t, _t, diff))
#       I wonder how this would affect runtime
#        __t = int(_t)
#        if (__t * __t == n):
#            return __t
        t = _t
    t = int(t)
    if (t * t == n):
        return t
    return -1

def tToP (t):
    va = intHeron(1 + (12 * ((t * t) + t)))
    if (va == -1 or (1 + va) % 6 != 0):
        return -1
    return int((1 + va)/6)

def tToH (t):
    va = intHeron(1 + (4 * ((t * t) + t)))
    if (va == -1 or (1 + va) % 4 != 0):
        return -1
    return (1 + va)/4

#   This found the solution 
#i = 285
#found = False
#while (not found):
#    i += 1
#    if (tToP(i) != -1 and tToH(i) != -1):
#        found = True

def findMatchingNumbers(upto):
    ret = set()
    tI = 0
    while (tI < upto):
        tI += 1
        pI = tToP(tI)
        hI = tToH(tI)
        if (pI != -1 and hI != -1):
            T = calcT(tI)
            P = calcP(pI)
            H = calcH(hI)
            ret.add((tI, T, pI, P, hI, H))
    return ret




