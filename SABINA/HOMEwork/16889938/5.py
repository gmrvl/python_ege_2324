r = 0
for i in range(100, 1000):
    s = str(i)
    a1 = int(s[0])
    a2 = int(s[1])
    a3 = int(s[2])
    pr1 = a1 * a2
    pr2 = a2 * a3
    if pr1 < pr2:
        r = str(pr1) + str(pr2)
    else:
        r = str(pr2) + str(pr1)
    if r == '621':
        print(i)
