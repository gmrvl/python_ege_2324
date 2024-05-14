for i in range(0,10000):
    n = int(bin(i)[2:])

    if i % 5 == 0:
        r = int(str(n) + str(bin(5)[2:]))
    elif i % 7 == 0:
        r = int(str(n) + str(bin(7)[2:]))
    else:
        r = int(str(n) + '1')
    if r < 1728404:
        print(n)





