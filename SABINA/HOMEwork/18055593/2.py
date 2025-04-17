def f(x,a):
    return x % a == 0

a = 1
while True:
    for x in range(1,100000):
        if not(f(120,a) and ((not f(x,a)) <= (f(x,18) <= (not f(x,24))))):
            break
    else:
        print(a)
    a += 1