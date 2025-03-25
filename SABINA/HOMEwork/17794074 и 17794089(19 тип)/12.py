for i in range(49,1000):
    b = '0' + i * '2' + '1' * 48 + '0'
    while not ('00' in b):
        b = b.replace('02', '101', 1)
        b = b.replace('11', '2', 1)
        b = b.replace('012', '30', 1)
        b = b.replace('010', '00', 1)

    summ = b.count('1') + b.count('2')*2 + b.count('3') * 3
    dells = []
    for k in range(2, int(summ**0.5) + 1):
        if summ % k == 0:
            dells.append(1)
            break
    print(summ, dells)
    print(b)
    if len(dells) == 0:
        print(i)
        break