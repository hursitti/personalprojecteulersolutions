def getDigit(x, index):
    ret = x % (10**index)
    ret = ret / (10**(index - 1))
    return ret

def palinLen (x):
    digits = 1
    div = 10
    while (x / div > 0):
        digits += 1
        div *= 10
    return digits

def isPalin (num):
    L = palinLen (num)
    for x in range(1, (L/2) + 1):
        if (getDigit(num, x) != getDigit(num, (L - (x - 1)))):
            return False
    return True


m = 0

i = 100
while i < 1000:
    j = 100
    while j < 1000:
        x = i * j
        if (isPalin(x) and x > m):
            m = x
        j += 1
    i += 1

print (m)
