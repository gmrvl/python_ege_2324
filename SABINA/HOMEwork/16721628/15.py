# х&А → (x&36 = 0 → х&6)
for a in range(0, 1000):
    fl = True
    for x in range(0, 1000):
        f = (x&a != 0) <= ((x&36 == 0) <= (x&6 != 0))
        if not f:
            fl = False
    if fl:
        print(a)
