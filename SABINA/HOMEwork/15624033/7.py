for i in range(1, 100000):
    n = bin(i)[2:]
    summ = n.count('1')
    if summ % 2 == 1:
        n = n + '10'
    else:
        n = n + '00'
    R = int(n, 2)
    if R > 441:
        print(R)
        break
# не сумма 1 , а просто число
