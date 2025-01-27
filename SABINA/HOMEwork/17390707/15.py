for a in range(1000):
    fl = True
    for x in range(1000):
        for y in range(1000):
            f = ((x + 3*y) > a) or (y<30) or (x<30)
            if not f:
                fl = False
    if fl:
        print(a)