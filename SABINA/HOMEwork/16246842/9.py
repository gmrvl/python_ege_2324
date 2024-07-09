for i in range(1, 10000):
    n = bin(i)[2:]
    summ = n.count('1')
    if summ % 2 == 0:
        n = n + '1'
    else:
        n += '0'
    r = int(n,2)
    if r > 54:
       print(r)
       break