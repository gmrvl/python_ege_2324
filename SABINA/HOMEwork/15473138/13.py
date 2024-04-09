for i in range(10000,100000):
    s = str(i)
    a1 = int(s[0])
    a2 = int(s[1])
    a3 = int(s[2])
    a4 = int(s[3])
    a5 = int(s[4])
    sum1 = a1 + a3 + a5
    sum2 = a2 + a4
    if sum1 < sum2:
        n = str(sum1) + str(sum2)
    else:
        n = str(sum2) + str(sum1)
    if n == '621':
        print(i)
        break