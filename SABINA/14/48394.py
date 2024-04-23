for x in '0123456789':
    d1 = '4c' + x + '4'
    d2 = x + '62a'
    summ = int(d1, 15) + int(d2, 13)
    if summ % 121 == 0:
        print(summ // 121)