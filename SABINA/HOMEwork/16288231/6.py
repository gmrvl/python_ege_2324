for n in range(10000):
    r = bin(n)[2:]
    summ = r.count('1')
    if summ % 2 == 0:
        r += '1'
    if summ % 2 == 1:
        r += '0'
    summ = r.count('1')
    if summ % 2 == 0:
        r += '1'
    if summ % 2 == 1:
        r += '0'
    r = int(r,2)
    if r > 54:
        print(r)
        break
