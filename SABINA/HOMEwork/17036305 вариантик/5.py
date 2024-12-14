for n in range(1, 10000):
    r = bin(n)[2:]
    r =(str(r))[::-1]
#    print(r)
    while len(r) > 0 and r[0] == '0':
           r = r[1:]
    r = int(r,2)
    if n <= 100 and r == 11:
        print(n)

