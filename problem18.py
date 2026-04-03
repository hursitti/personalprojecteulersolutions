def createMaze(f):
    ret = []
    with open(f, 'r') as fi:
        for line in fi.readlines():
            ret.append([int(x) for x in line.split(" ")])
    return ret

def buildTree(maze, depth):
    def nextItem(ol):
        nex = ol[0]
        for item in ol:
            if item[2] > nex[2]:
                nex = item
        ol.remove(nex)
        return nex

    
    closedList = {(-1, -1) : (0, -1, -1)}
    openList = [(0, 0, maze[0][0], -1, -1)]
    leafs = []
    while len(openList) > 0:
        n = nextItem(openList)
        closedList[(n[0], n[1])] = (n[2], n[3], n[4])
        if (n[0] == 0 and n[1] == 0):
            print(n)
        if (n[0] < depth):
            if (n[0]+1, n[1]) not in closedList:
                openList.append((n[0] + 1, n[1], n[2] + maze[n[0] + 1][n[1]], n[0], n[1]))
            if (n[0]+1, n[1] + 1) not in closedList:
                openList.append((n[0] + 1, n[1] + 1, n[2] + maze[n[0] + 1][n[1] + 1], n[0], n[1]))
        else:
            leafs.append((n[0], n[1]))
    return (closedList, leafs)

def tracePath(node, cl):
    while not(node[1] == -1 and node[2] == -1):
        print (node)
        node = cl[(node[1], node[2])]

maze = createMaze("littletriangle.txt")
m2 = createMaze("smallertriangle.txt")
m3 = createMaze("solution.txt")

ret = buildTree(maze, len(maze) - 1)
ret2 = buildTree(m2, len(m2) - 1)
ret3 = buildTree(m3, len(m3) - 1)