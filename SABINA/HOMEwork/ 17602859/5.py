for i in range(1000,10000):
    s = str(i)
    a1 = s[0]
    a2 = s[1]
    a3 = s[2]
    a4 = s[3]
    summ1 = str(a1) + str(a2)
    summ2 = str(a2) + str(a3)
    summ3 = str(a3) + str(a4)
    if max(summ1,summ2,summ3) == summ1:
        if summ2 > summ3:
            r = summ3 + summ2
        if summ3 > summ2:
            r = summ2 + summ3
        if summ2 == summ3:
            r = summ3 + summ2
    if max(summ1,summ2,summ3) == summ2:
        if summ1 > summ3:
            r = summ3 + summ1
        if summ3 > summ1:
            r = summ1 + summ3
        if summ1 == summ3:
            r = summ3 + summ1
    if max(summ1,summ2,summ3) == summ3:
        if summ2 > summ1:
            r = summ1 + summ2
        if summ1 > summ2:
            r = summ2 + summ1
        if summ2 == summ1:
            r = summ1 + summ2
    if r == '1418':
        print(i)
