for n in range(10000):
    r = bin(n)[2:]
    summ = r.count('1')
    if summ % 2 == 0:
        r = r + '00'
    else:
        r = r + '10'
    r = int(r, 2)
    if r > 55:
        print(r)
        break