def odd (x):
    return x & 1 == 1

def collatzString (x):
    t = str(x)
    
    while (x != 1):
        if (odd(x)):
            x = (3*x) + 1
        else:
            x = x/2
        t += " " + str(x)
    return t

print (collatzString(13))

def collatzTotal (x):
    t = 1
    while (x != 1):
        if (odd(x)):
            x = (3*x) + 1
        else:
            x = x / 2
        t += 1
    return t

print (collatzTotal(13))

def dynCollatzTotal (x, rec):
    total = 1
    t = x
    while (t != 1):
        if (odd(t)):
            t = (3*t) + 1
        else:
            t = t / 2
        if (t in record):
            record[x] = total + record[t]
            return record[x]
        else:
            total += 1
    record[x] = total
    return total

record = dict()
print(dynCollatzTotal(13, record))

def largestInRecord(rec):
    maxIndex = 1
    for i in rec:
        if rec[i] > rec[maxIndex]:
            maxIndex = i
    return maxIndex

def buildRecord(limit, rec):
    x = 1
    while (x < limit):
        dynCollatzTotal(x, rec)
        x += 1

buildRecord (1000000, record)
print(largestInRecord(record))





