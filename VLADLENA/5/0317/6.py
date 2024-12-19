for i in range(1000, 100000):
    a = str(i)
    n1 = int(a[1]) + int(a[2])
    n2 = int(a[2]) + int(a[3])
    n3 = int(a[3]) + int(a[4])
    sum1 = a[1]
    sum2 = a[2]
    sum3 = a[3]
    maxx = str(max(sum1, sum2, sum3))
    aver = str((sum1, sum2, sum3) - maxx - min(sum1, sum2, sum3))
    res = aver + maxx
    if res == '1517':
        print(i)
        break