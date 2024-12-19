for i in range(100, 10000):
    a = str(i)
    n1 = int(a[1]) + int(a[2])
    n2 = int(a[3]) + int(a[4])
    if n1 < n2:
        res = str(n1) + str(n2)
    else:
        res = str(n2) + str(n1)
    if res == '621':
        print(i)
        break