for i in range(1000, 10000, 2):
    s = str(i)
    a1 = int(s[0])
    a2 = int(s[1])
    a3 = int(s[2])
    a4 = int(s[3])
    summ1 = a1 + a2
    summ2 = a3 + a4
    if summ1< summ2:
        n = str(summ1) + str(summ2)
    else:
        n = str(summ2) + str(summ1)
    if n == '616':
        print(i)