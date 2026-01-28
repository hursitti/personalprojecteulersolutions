import math
import time

def pent(index):
    return int(index * ((index * 3) - 1)/2)

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

def intNative(n):
    t = math.sqrt(n)
    if (t == math.floor(t)):
        return int(t)
    return -1

numbers = 1000000
i = 1
tempH = []
tempN = []
cTimeH = 0
cTimeN = 0
tempTime = time.time()
while i < numbers:
    tempH.append(intHeron(i))
    i += 1
cTimeH += time.time() - tempTime

i = 1
tempTime = time.time()
while i < numbers:
    tempN.append(intNative(i))
    i += 1

i = 0
while i < len(tempH):
    if tempH[i] != tempN[i]:
        print ("Error at " + i)
    i += 1

cTimeN += time.time() - tempTime

print( "H:" + repr(cTimeH) + ", N:" + repr(cTimeN))
