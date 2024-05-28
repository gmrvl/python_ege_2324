for i in range(10000, 100000):
    s = str(i)
    a1 = int(s[0])
    a2 = int(s[1])
    a3 = int(s[2])
    a4 = int(s[3])
    a5 = int(s[4])
    sum1 = int(a1) + int(a3) + int(a5)
    sum2 = int(a2) + int(a4)
    if sum1 < sum2:
        n = str(sum1) + str(sum2)
    else:
        n = str(sum2) + str(sum1)
    if n == '621':
        print(i)
        break
