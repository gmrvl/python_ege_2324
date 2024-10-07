for n in range(0,10000):
    r = bin(n)[2:]
    r = r.replace('0','*')
    r = r.replace('1', '0')
    r = r.replace('*','1')
    while r[0] == 0 and len(r) > 0:
        r = r[1:]
    r = int(r,2)
    r = n - r
    if r == 999:
        print(n)
