ret = 0
with open("13.txt", 'r') as fi:
    for line in fi.readlines():
        ret += int(line)
print(ret)