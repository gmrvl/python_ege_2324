for i in range(1000, 10000):
    n = i
    a = []
    while n != 0:
        a.append(n % 10)
        n //= 10
    s1 = a[3] + a[2]
    s2 = a[2] + a[1]
    s3 = a[1] + a[0]
    sums = sorted([s1, s2, s3])
    res = str(sums[1]) + str(sums[2])
    if res == '1517':
        print(i)
