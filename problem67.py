def createMaze(f):
    ret = []
    with open(f, 'r') as fi:
        for line in fi.readlines():
            ret.append([int(x) for x in line.split(" ")])
    return ret

def buildTree(maze, depth):
    closedList = {(0, 0) : (maze[0][0], -1, -1)}
    n = 1
    while n < depth:
        width = len(maze[n])
        i = 0
        while i < width:
            if i != 0:
                if i < width - 1:
                    up = closedList[(n-1, i)]
                    across = closedList[(n-1, i-1)]
                    if (up[0] > across[0]):
                        closedList[(n, i)] = (up[0] + maze[n][i], n-1, i)
                    else:
                        closedList[(n, i)] = (across[0] + maze[n][i], n-1, i-1)
                else:
                    closedList[(n, i)] = (closedList[(n-1, i-1)][0] + maze[n][i], n-1, i-1)
            else:
                closedList[(n, i)] = (closedList[(n-1, i)][0] + maze[n][i], n-1, i)
            i += 1
        n += 1
    
    return closedList

def leafMax (tree, depth):
    d = depth - 1
    leafs = [tree[(d, x)] for x in range(depth)]
    leafs.sort()
    return leafs

maze = createMaze("littletriangle.txt")
m2 = createMaze("smallertriangle.txt")
m3 = createMaze("solution.txt")
m4 = createMaze("0067_triangle.txt")

ret = buildTree(maze, len(maze))
ret2 = buildTree(m2, len(m2))
ret3 = buildTree(m3, len(m3))
r4 = buildTree(m4, len(m4))