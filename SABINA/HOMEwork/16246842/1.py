for i in range(1, 10000):
    n = bin(i)[2:]
    summ = n.count('1')
    if summ % 2 == 1:
        n += '10'
    else:
        n += '00'
    r = int(n, 2)
    if r > 97:
        print(r)
        break

