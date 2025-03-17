for i in range(49,1000):
    a = '0' + '1' * 48 + i * '2'
    summ = 0
    b = 0
    fl = True
    while '00' not in a:
        b = a.replace('02', '101', 1)
        b = a.replace('11', '2', 1)
        b = a.replace('012', '30', 1)
        b = a.replace('010', '00', 1)
    while b > 0:
        summ = b % 10
        b = b // 10
        for k in range(2,(b**0.5) + 1):
            if b <= 1:
                fl = False
            if b % k == 0:
                fl = False
            else:
                fl = True
    if fl:
        print(i)