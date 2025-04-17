for x in [i * 0.25 for i in range(-1000,1000)]:
    P = 24 <= x <= 77
    Q = 47 <= x <= 92
    R = 82 <= x <= 116
    a = 0
    f = (not( Q <= (P or R))) <= (not a) <= (not Q)
    if f != 1:
        print(x)