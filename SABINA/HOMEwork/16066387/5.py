for i in range(100, 1000):
    s = str(i)
    a1 = int(s[0])
    a2 = int(s[1])
    a3 = int(s[2])
    sum1 = a1 + a2
    sum2 = a2 + a3
    if sum1 < sum2:
        n = str(sum1) + str(sum2)
    else:
        n = str(sum2) + str(sum1)
    if n == '1115':
        print(i)
        break


