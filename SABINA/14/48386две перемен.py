for x in '0123456789abcde':
    for y in '0123456789abcde':
        d1 = '90' + x + '4' + y
        d2 = '91' + x + y + '2'
        summ = int(d1, 15) + int(d2, 16)
        if summ % 56 == 0:
            print(summ // 56)