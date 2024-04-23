for x in '012345678':
    for y in '012345678':
        d1 = '88' + x + '4' + y
        d2 = '7' + x + '44' + y
        summ = int(d1, 9) + int(d2, 11)
        if summ % 61 == 0:
            print(summ // 61)
