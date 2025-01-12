fl = True
for a in range(1000):
    for x in range(0, 1000):
        for p in range(10,30):
            for q in range(13, 19):
                f = ((str(x) in str(a)) <= (str(x) in str(p))) or (str(x) in str(q))
                if not f:
                    fl = False
    if fl:
        print(a)

