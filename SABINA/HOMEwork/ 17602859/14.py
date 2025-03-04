minn = 10000
for x in '0123456789abc':
    for y in '0123456789abc':
        d1 = '8'+ x + '78' + y
        d2 = '79' + x + y + '7'
        summ = int(d1,13) + int(d2,18)
        print(summ // 9)