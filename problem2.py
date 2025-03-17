cur = 1
pre = 1
s = 0

while cur < 4000000:
    if (cur % 2 == 0):
        s += cur
    print(cur)
    temp = cur
    cur = cur + pre
    pre = temp

print(s)
