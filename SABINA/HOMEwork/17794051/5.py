for n in range(1, 1000):
    a = 0
    while n > 0:
        a = str(n % 3) + str(a)
        n = n // 3
    while n > 0:
        a = str(n % 3) + str(a)
        n = n // 3
    r = int(a,3)
    print(r)