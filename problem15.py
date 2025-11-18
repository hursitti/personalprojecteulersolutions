def pathSearchRec(maxX, maxY, x, y):
    total = 0
    if (x < maxX):
        total += pathSearchRec(maxX, maxY, x + 1, y)
    if (y < maxY):
        total += pathSearchRec(maxX, maxY, x, y + 1)
    if (x == maxX and y == maxY):
        return 1
    return total

def pathSearch(maxX, maxY):
    return pathSearchRec(maxX, maxY, 0, 0)

def dynPathSearchRec(maxX, maxY, x, y, rec):
    total = 0
    if ((maxX, maxY, x, y) in rec):
        return rec[(maxX, maxY, x, y)]
    if (x < maxX):
        total += dynPathSearchRec(maxX, maxY, x + 1, y, rec)
    if (y < maxY):
        total += dynPathSearchRec(maxX, maxY, x, y + 1, rec)
    if (x == maxX and y == maxY):
        rec[(maxX, maxY, x, y)] = 1
        return 1
    rec[(maxX, maxY, x, y)] = total
    return total

def dynPathSearch(maxX, maxY, rec):
    return dynPathSearchRec(maxX, maxY, 0, 0, rec)
