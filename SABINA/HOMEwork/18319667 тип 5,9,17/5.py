for n in range(1, 1000000):
    r = bin(n)[2:]
    if n%5 == 0:
        r += str(bin(5)[2:])
    else:
        r += '1'
    if int(r,2)%7 == 0:
        r += str(bin(7)[2:])
    else:
        r += '1'

    if int(r, 2) < 1728404:
        print(n)