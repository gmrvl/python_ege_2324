
for n in range(100,1000):
    r = 0
    n = str(n)
    a1 = int(n[0])
    a2 = int(n[1])
    a3 = int(n[2])
    pr1 = a1 * a2
    pr2 = a2 * a3
    if pr1 > pr2:
        r = str(pr2)+str(pr1)
    else:
        r = str(pr1)+str(pr2)
    if r == '621':
        print(n)
