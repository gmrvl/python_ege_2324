for i in range(1, 1000):
    n = i
    a = ''
    while n > 0:
        a = str(n % 3) + str(a)
        n = n // 3
    a += str(i%3)
    r = int(a,3)
    print(r)