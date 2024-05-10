for i in range(100, 1000):
    s = str(i)
    a1 = s[0]
    a2 = s[1]
    a3 = s[2]
    pr1 = int(a1) * int(a2)
    pr2 = int(a2) * int(a3)
    if pr1 < pr2:
        n = str(pr2) + str(pr1)
    else:
        n = str(pr1) + str(pr2)
    if n == '1412':
        print(i)
        break