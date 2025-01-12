for i in range(1, 100000):
    r = bin(i)[2:]
    summ = 0
#    summ = r.count('1')
    while i != 0:
       summ += i % 10
       i = i // 10
    if summ % 2 == 1:
        r = str(r) + '1'
    else:
        r = str(r) + '0'


    r = int(r,2)
    k = bin(r)[2:]
    summ = 0
    while r != 0:
       summ += r % 10
       r = r // 10
    if summ % 2 == 1:
        k = str(k) + '1'
    else:
        k = str(k) + '0'


    r = int(k, 2)
    l =  bin(r)[2:]
    summ = 0
    while r != 0:
        summ += r % 10
        r = r // 10
    if summ % 2 == 1:
        r = str(l) + '1'
    else:
        r = str(l) + '0'


    r = int(l,2)
    if r > 1028:
        print(r)


