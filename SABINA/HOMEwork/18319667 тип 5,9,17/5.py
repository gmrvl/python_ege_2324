for n in range(1,1000):
    r = bin(n)[2:]
    if n%5 == 0:
        r = str(r) + str(bin(5)[2:])
        if int(r)%7 == 0:
            r = str(r) + str(bin(7)[2:])
        else:
            r = str(r) + '1'
    else:
        r = str(r) + '1'
        if int(r)%7 == 0:
            r = str(r) + str(bin(7)[2:])
        else:
            r = str(r) + '1'
    a = ''
    while int(r) > 0:
        a = str(int(r)%10)+str(a)
        r = int(r) // 10
    if int(a) < 1728404:
        print(n)