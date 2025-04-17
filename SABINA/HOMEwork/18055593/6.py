def f(x,a):
    return x % a == 0


a = 1
while True:
    for x in range(1,100000):
        B = 70 <= x <= 90
        if not(f(x,a) or (B <= (not f(x,27)))):
            break
    else:
        print(a)
    a += 1
