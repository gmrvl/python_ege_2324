for i in range(1,100000):
    n = bin(i)[2:]
    if int(n) % 5 == 0:
        n = str(n) + '0'
    else:
        n = str(n) + '1'
    summ = n.count('1')
    r = str(summ) + str(summ % 2)
    r = int(r)
    if r > 105:
        print(r)