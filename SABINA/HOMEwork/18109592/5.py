for n in range(1,10000):
    i = n
    r = ''
    while i > 0:
        r = str(i%3) + r
        i = i // 3
    r = r + str(n%3)
    r = int(r,3)
    if 1000 <= r <= 9999:
        print(r)