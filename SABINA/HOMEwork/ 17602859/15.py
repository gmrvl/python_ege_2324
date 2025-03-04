fl = True
for a in range(0,1000):
    for x in range(0,1000):
        for y in range(0, 1000):
            f = ((2*x + y) != 70) or (x < y) or (a < x)
            if not f:
                fl = False
    if fl:
        print(a)

