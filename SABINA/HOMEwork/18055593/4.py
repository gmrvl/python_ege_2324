for x in [i * 0.25 for i in range(-10000,10000)]:
    P = 23 <= x <= 58
    Q = 1 <= x <= 39
    A = 0
    f = (P or A) <= (Q or A)
    if f != 1:
        print(x)