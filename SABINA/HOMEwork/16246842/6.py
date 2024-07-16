for i in range(1, 10000):
    n = bin(i)[2:]
    summ = n.count('1')
    if summ % 2 == 1:
        n = n + str(summ % 2)
    else:
        n += str(summ % 2)
    r = int(n, 2)
    if r > 396:
        print(r)
        break
