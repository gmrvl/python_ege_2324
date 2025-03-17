for a in range(1000):
    fl = True
    for x in range(100):
        for y in range(100):
            f = ((x < a) <= (x**2 < 81)) and ((y**2 <= 36) <= (y <= a))
            if not f:
                fl = False
    if fl:
        print(a)

