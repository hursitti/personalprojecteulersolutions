from collections import deque

raw = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08\n\
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00\n\
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65\n\
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91\n\
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80\n\
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50\n\
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70\n\
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21\n\
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72\n\
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95\n\
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92\n\
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57\n\
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58\n\
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40\n\
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66\n\
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69\n\
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36\n\
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16\n\
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54\n\
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"

rawTemp = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08\n\
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00\n\
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65\n\
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91\n\
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80\n\
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50\n\
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70\n\
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21\n\
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72\n\
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95\n\
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92\n\
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57\n\
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58\n\
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40\n\
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66\n\
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 99\n\
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 99 99\n\
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 99 99 16\n\
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 99 99 05 54\n\
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 99 99 19 67 48"

def parseData(rawData):
    ret = []
    spl = rawData.split("\n")
    height = len(spl)
    for row in spl:
        spl2 = row.split(" ")
        width = len(spl2)
        for item in spl2:
            ret.append(int(item))
    return (ret, height, width)

parsed, height, width = parseData(rawTemp)

class Counter:
    def __init__(self, firstValues):
        self.maxValue = long(-1)
        self.currentValue = 1
        self.zeros = 0
        self.queue = deque()
        for x in firstValues:
            self.queue.append(x)
            if (x == 0):
                self.zeros += 1
            else:
                self.currentValue *= x
            if (self.zeros == 0):
                self.maxValue = self.currentValue

    def newValue(self, x):
        self.prev = self.queue.popleft()
        if (x == 0):
            self.zeros += 1
        else:
            self.currentValue *= x
            
        if (self.prev == 0):
            self.zeros -= 1
        else:
            self.currentValue /= self.prev
        
        if (self.zeros == 0 and self.currentValue > self.maxValue):
            self.maxValue = self.currentValue
        
        self.queue.append(x)

    def hasZeros(self):
        return zeros > 0

def check(c, _m, _x, _y, _indexx, _indexy):
    if (c.maxValue > _m):
        return (c.maxValue, _x, _y)
    return (_m, _indexx, _indexy)

def getFromIndex(data, x, y, width):
    return data[(y * width) + x]

def horizontalPass(data, height, width, answerLength):
    m = long(-1)
    indexx = -1
    indexy = -1
    
    for y in range(0, height):
        counter = Counter(data[(y*width):((y*width)+answerLength)])
        m, indexx, indexy = check(counter, m, 0, y, indexx, indexy)
        for x in range(answerLength, width):
            counter.newValue(getFromIndex(data, x, y, width))
            m, indexx, indexy = check(counter, m, x + 1 - answerLength, y, indexx, indexy)
    
    return m, indexx, indexy

def verticalPass(data, height, width, answerLength):
    m = long(-1)
    indexx = -1
    indexy = -1

    for x in range(0, width):
        counter = Counter([getFromIndex(data, x, _y, width) for _y in range(answerLength)])
        m, indexx, indexy = check(counter, m, x, 0, indexx, indexy)
        for y in range(answerLength, height):
            counter.newValue(getFromIndex(data, x, y, width))
            m, indexx, indexy = check(counter, m, x, y + 1 - answerLength, indexx, indexy)

    return m, indexx, indexy

def sePass(data, height, width, answerLength):
    m = long(-1)
    indexx = -1
    indexy = -1

    for row in range(height - answerLength):
        counter = Counter([getFromIndex(data, 0 + t, row + t, width) for t in range(answerLength)])
        m, indexx, indexy = check(counter, m, 0, row, indexx, indexy)
        
        x, y = answerLength, row + answerLength
        while y < height and x < width:
            counter.newValue(getFromIndex (data, x, y, width))
            m, indexx, indexy = check(counter, m, x + 1 - answerLength, y + 1 - answerLength, indexx, indexy)
            x += 1
            y += 1

    for column in range(1, width - answerLength):
        counter = Counter([getFromIndex(data, column + t, 0 + t, width) for t in range(answerLength)])
        m, indexx, indexy = check(counter, m, column, 0, indexx, indexy)
        
        x, y = column + answerLength, answerLength
        while y < height and x < width:
            counter.newValue(getFromIndex (data, x, y, width))
            m, indexx, indexy = check(counter, m, x + 1 - answerLength, y + 1 - answerLength, indexx, indexy)
            x += 1
            y += 1

    return m, indexx, indexy

def swPass(data, height, width, answerLength):
    m = long(-1)
    indexx = -1
    indexy = -1

    for column in range(answerLength - 1, width):
        counter = Counter([getFromIndex(data, answerLength - (1 + t), 0 + t, width) for t in range(answerLength)])
        m, indexx, indexy = check(counter, m, answerLength - 1, 0, indexx, indexy)
        
        x, y = column - answerLength, answerLength
        while y < height and x > -1:
            counter.newValue(getFromIndex (data, x, y, width))
            m, indexx, indexy = check(counter, m, x + answerLength - 1, y + 1 - answerLength, indexx, indexy)
            x -= 1
            y += 1

    for row in range (1, height):
        counter = Counter([getFromIndex(data, width - (1 + t), 1 + t, width) for t in range(answerLength)])
        m, indexx, indexy = check(counter, m, width + 1 - answerLength, 0, indexx, indexy)
        
        x, y = width - answerLength, answerLength
        while y < height and x > -1:
            counter.newValue(getFromIndex (data, x, y, width))
            m, indexx, indexy = check(counter, m, x + answerLength - 1, y + 1 - answerLength, indexx, indexy)
            x -= 1
            y += 1

    return m, indexx, indexy

#result, x, y = horizontalPass(parsed, height, width, 4)
print(horizontalPass(parsed, height, width, 4))
print(verticalPass(parsed, height, width, 4))
print(sePass(parsed, height, width, 4))
print(swPass(parsed, height, width, 4))

































