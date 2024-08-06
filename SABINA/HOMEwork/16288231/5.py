for n in range(10000):
    r = bin(n)[2:]
    s = str(r)
    summ = sum(map(int, s))
    if summ % 2 == 1:
        s += '1'
    if summ % 2 == 0:
        s += '0'

    summ = sum(map(int, s))
    if summ % 2 == 1:
        s += '1'
    if summ % 2 == 0:
        s += '0'

    summ = sum(map(int, s))
    if summ % 2 == 1:
        s += '1'
    if summ % 2 == 0:
        s += '0'
    r = int(s , 2)
    if r > 1028:
        print(r)
        break
