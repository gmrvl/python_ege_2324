# 123x5 + 1x233
for x in '0123456789abcde':
    d1 = '123' + x + '5'
    d2 = '1' + x + '233'
    summ = int(d1, 15) + int(d2, 15)
    if summ % 14 == 0:
        print(summ // 14)