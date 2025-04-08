import math

def getNum(tripletSum):
    print("triplet sum of " + str(tripletSum))
    for a in range (0, tripletSum // 3):
        for b in range(a + 1, tripletSum // 2):
                c = math.sqrt((a*a)+(b*b))
                if (c % 1.0 == 0.0):
                    c = int(c)
                    if (a + b + c == tripletSum):
                        print (str(a) + " " + str(b) + " " + str(c))

getNum(1000)
getNum(12)
getNum(70)
getNum(132)
getNum(1000000)
