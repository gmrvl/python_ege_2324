for x in '0123456789abcdefg':
    sum1 = '8' + x + '5678'
    sum2 = '457' + x + '69'
    summ3 = '145' + x + '1'
    summ = int(sum1,25) + int(sum2, 25)
    if summ % 23 == 0:
        print(summ // 23)