for n in range(10000):
    s = bin(n)[2:]
    summ = s.count('1')
    if summ % 2 == 0:
        s += '00'
    if summ % 2 == 1:
        s += '10'
    s = int(s, 2)
    if s > 97:
        print(s)
        break