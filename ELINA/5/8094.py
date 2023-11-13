for n in range(10000):
    b_n = bin(n)[2:]
    summ = b_n.count('1')
    if summ % 2 == 0:
        b_n += '00'
    else:
        b_n += '10'
    r = int(b_n, 2)
    if r > 43:
        print(r)
        break



