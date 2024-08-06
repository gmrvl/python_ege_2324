for n in range(10000):
    s = bin(n)[2:]
    summ = s.count('1')
    if summ % 2 == 0:
        s += '0'
    if summ % 2 == 1:
        s += '1'
#    print(s)
    summ = s.count('1')
    if summ % 2 == 0:
        s += '0'
    if summ % 2 == 1:
        s += '1'
#    print(s)
    s = int(s, 2)
    if s > 396:
        print(s)
        break