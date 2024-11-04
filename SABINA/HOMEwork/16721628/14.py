# 12·34= xy2
for p in range(1,10):
    for x in range(1, p):
        for y in range(0, p):
            a1 = (1*p**1 + 2*p**0)* (3*p**1 + 4*p**0)
            a2 = x*(p**2) + y*(p**1) + 2
            if a1 == a2:
                print(y*(p**1)+x*(p**0))

