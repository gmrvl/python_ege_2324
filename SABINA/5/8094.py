for i in range(0, 10000):
    n = bin(i)[2:]
    summ = n.count('1')
    if summ % 2 == 0:
        n += '00'    # из-за того, что просят повоторить действие. тут не меняется кол-во 1
    else:
        n += '10'    # а тут меняется, потому что нечетное на 2 даст '1' в строку
    r = int(n, 2)
    if r > 43:
        print(r)
        break
