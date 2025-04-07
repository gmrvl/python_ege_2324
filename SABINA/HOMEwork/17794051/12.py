for n in range(3,10001):
    summ = 0
    s ='5' + n * '2'
    while '52' in s or '1122' in s or '2222' in s:
        if '52' in s:
            s = s.replace('52','11',1)
        if '2222' in s:
            s = s.replace('2222','5',1)
        if '1122' in s:
            s = s.replace('1122','25', 1)

    summ = s.count('5')*5 + s.count('2')*2 + s.count('1')
    if summ == 64:
        print(n)
