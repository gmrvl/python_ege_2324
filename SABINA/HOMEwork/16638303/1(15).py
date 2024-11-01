for a in range(0, 1000):
    fl = True
    for x in range(0, 1000):
        f = x&a != 0 <= ( x&10 == 0 <= x&3 != 0)
        if not f:
            fl = False
            if fl:
                print(a)
