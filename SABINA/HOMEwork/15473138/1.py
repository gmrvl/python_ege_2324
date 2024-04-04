count = 0
for i in range(1000, 10000):
    s = str(i)
    a1 = int(s[0])
    a2 = int(s[1])
    a3 = int(s[2])
    a4 = int(s[3])
    if a1 % 2 == 1 and a2 % 2 == 1 and a3 % 2 == 1 and a4 % 2 == 1:
        sum1 = a1 + a2
        sum2 = a3 + a4
        if sum1 < sum2:
            n = str(sum1) + str(sum2)
        else:
            n = str(sum2) + str(sum1)
        if n == '414':
            count += 1
print(count)