for p in range(1, 10):
    for x in range(1, p):
        for y in range(0, p):
            for z in range(1, p):
                for w in range(1, p):
                    t1 = z*p**4+x*p**3+y*p**2+x*p**1+4
                    t2 = x*p**4+y*p**3+6*p**2+5*p**1+8
                    t3 = w*p**4+z*p**3+x*p**2+7*p**1+3
                    if t1 + t2 == t3:
                        print(x*p**3+y*p**2+z*p**1+w*p**0)