for n in  range(10000):
    r = bin(n)[2:]
    summ = r.count('1')
    if summ % 2 == 0:
        r += '10'
    else:
        r += '01'
    r = int(r, 2)
    if r < 109:
        print(r)
