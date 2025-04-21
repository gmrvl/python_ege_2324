for t in range(1, 10000):
    i = t
    n = ''
    while i != 0:
        n = str(i%4) + n
        i //= 4
    if t % 4 == 0:
        n = n[-2:] + n
    elif t % 3 == 0 and t > 3:
        n = n + n[:2]
    else:
        n0 = int(n)
        n = ''
        while n0 != 0:
            n += str(n0 % 10)
            n0 //= 10
    r = int(n, 4)
    if r < 25:
        print(t)





