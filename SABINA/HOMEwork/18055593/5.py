for x in [ i*0.25 for i in range(-10000,10000)]:
    P = 130 <= x <= 171
    Q = 160 <= x <= 185
    A = 0
    f = (P <= (Q and (not A) <= (not P)))
    if f != 1:
        print(x)