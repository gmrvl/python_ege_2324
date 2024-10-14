#8x834+44x27
for x in '0123456789abcdef':
    d1 = '8' + x +'834'
    d2 = '44' + x + '27'
    summ = int( d1, 16) + int(d2, 16)
    if summ % 23 == 0 :
        print(summ // 23)
