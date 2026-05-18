import math

def rectanglePermutations(x, y, maxX, maxY):
    return ((maxX - x) + 1) * ((maxY - y) + 1)

def gridRectangleNumber(maxX, maxY):
    x = 0
    total = 0
    while (x < maxX):
        x += 1
        y = 0
        while (y < maxY):
            y += 1
            total += rectanglePermutations(x, y, maxX, maxY)
    return total

def grnTuple(tup):
    return gridRectangleNumber(tup[0], tup[1])

def rectSearch (targetSum):
    lowBound = (0, 0)
    lowBoundSum = 0
    highBound = (1, 1)
    highBoundSum = 1
    while (highBoundSum < targetSum):
        lowBound = highBound
        highBound = (lowBound[0] + 1, lowBound[1] + 1)
        highBoundSum = grnTuple(highBound)
    
    lowBoundSum = grnTuple(lowBound)

    minDiffGrid = lowBound if abs(lowBoundSum - targetSum) < abs(highBoundSum - targetSum) else highBound
    #could just grab from original
    minDiffGridSum = grnTuple(minDiffGrid)
    minDiffGridDiff = abs(minDiffGridSum - targetSum)

    #print(lowBound)
    #print(highBound)

    squareNum = highBound[1]
    y = squareNum - 1
    while (y > 1):
        #b = int((a*squareNum)/(1+squareNum-a))
        #upperbound of possible lower values from the quadratic which the 'rect number' always grows faster than and is greater than, and x^2 < (x-a)(x+b) when b > ax/(x-a)
        x = squareNum + int(((squareNum-y)*squareNum)/(y+1))
        newSum = gridRectangleNumber(x, y)
        while (newSum > lowBoundSum):
            newSum = gridRectangleNumber(x, y)
            if (minDiffGridDiff > abs(newSum - targetSum)):
                minDiffGrid = (x, y)
                minDiffGridSum = newSum
                minDiffGridDiff = abs(newSum - targetSum)
            x -= 1
        y -= 1

    return minDiffGrid
            
