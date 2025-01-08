for i in range(1, 100000):
    r = bin(i)[2:]
#    summ = 0
    summ = r.count('1')
#    for k in r:
#        summ += int(k)
    if summ % 2 == 1:
        r = str(r) + '100'
    else:
        r = str(r) + '000'
    r = int(r,2)
    if r > 1028:
        print(r)

