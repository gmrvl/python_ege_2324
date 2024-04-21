for i in range(1000,10000):
    s = str(i)
    a1 = int(s[0])
    a2 = int(s[1])
    a3 = int(s[2])
    a4 = int(s[3])
    sum1 = a1 + a2
    sum2 = a2 + a3
    sum3 = a3 + a4
    minn = min(sum2, sum3, sum1)
    maxx = max(sum2, sum3, sum1)
    sr = sum1 + sum2 + sum3 - maxx - minn
    n = str(sr) + str(maxx)
    if n == '1517':
        print(i)
        break