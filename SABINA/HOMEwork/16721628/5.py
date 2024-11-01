
for n in range(10000):
    l = ''
    r = bin(n)[2:]
    summ = r.count('1')
    r = list(r)
    if summ % 2 == 0:
        r += '0'
        r[0] = '1'
        r[1] = '0'
    else:
        r += '1'
        r[0] = '1'
        r[1] = '1'
    l = l.join(r)

    res = int(l, 2)
    if res > 40:
        print(n)
    break