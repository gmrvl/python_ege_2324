for a in range(0,1000):
    fl = True
    for x in range(0,100):
        for y in range(0,100):
            f = (x + 2*y < a) or (y > x) or (x > 30)
            if not f:
                fl = False
    if fl:
        print(a)