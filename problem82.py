def createSumMaze(f):
    ret = []
    with open(f, 'r') as fi:
        for line in fi.readlines():
            ret.append([int(x) for x in line.split(",")])
    return ret

def genericBFS(maze, endX, endY):
    def nextItem(ol):
        nex = ol[0]
        for item in ol:
            if item[2] < nex[2]:
                nex = item
        ol.remove(nex)
        return nex

    
    closedList = {(-1, -1) : (0, -1, -1)}
    openList = [(0, x, maze[x][0], -1, -1) for x in range(len(maze[0]))]
    while len(openList) > 0:
        n = nextItem(openList)
        closedList[(n[0], n[1])] = (n[2], n[3], n[4]) 
        if (n[0] == endX):
            return (closedList, n)
        if (n[0] < endX and (n[0]+1, n[1]) not in closedList):
            openList.append((n[0] + 1, n[1], n[2] + maze[n[1]][n[0] + 1], n[0], n[1]))
        if (n[1] < endY and (n[0], n[1]+1) not in closedList):
            openList.append((n[0], n[1] + 1, n[2] + maze[n[1] + 1][n[0]], n[0], n[1]))
        if (n[1] > 0 and (n[0], n[1]-1) not in closedList):
            openList.append((n[0], n[1] - 1, n[2] + maze[n[1] - 1][n[0]], n[0], n[1]))
    raise Exception("Goal was never reached")

def traceCLPath(closedList, startX, startY):
    path = []
    x = startX
    y = startY
    while x != -1 and y != -1:
        path.append((x, y))
        tempX = x
        x = closedList[(x, y)][1]
        y = closedList[(tempX, y)][2]
    return path

m = createSumMaze("0082_matrix.txt")
clPlus = genericBFS(m, 79, 79)
path = traceCLPath(clPlus[0], clPlus[1][0], clPlus[1][1])
