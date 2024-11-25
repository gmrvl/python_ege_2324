
for a in range(0, 1000):
    fl = True
    for x in range(0, 1000):
        f = (x&51 == 0) or ((x&41 ==0) <= (x&a == 0))
        if not f:
            fl = False
    if fl:
        print(a)
