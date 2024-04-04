for i in range(1000,10000):
    s = str(i)
    a1 = int(s[0])
    a2 = int(s[1])
    a3 = int(s[2])
    a4 = int(s[3])
    sum1 = a1 + a2
    sum2 = a2 + a3
    sum3 = a3 + a4
    if sum1 < sum2 < sum3:
        if sum2 < sum3:
            n = str(sum2) + str(sum3)
        else:
            n = str(sum3) + str(sum2)
    elif sum2 < sum1 < sum3:
        if sum2 < sum1:
            n = str(sum2) + str(sum1)
        else:
            n = str(sum1) + str(sum2)
    else:
        if sum1 > sum2:
            n = str(sum1) + str(sum2)
        else:
            n = str(sum2) + str(sum1)
        if n == '1418':
            print (i)