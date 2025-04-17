
for x in [i * 0.25 for i in range(-10000,10000)]:
    P = 19 <= x <= 84
    Q = 4 <= x <= 51
    a = 0
    f = Q <= ((not P)<= (not( Q and (not a))))
    if f != 1:
        print(x)