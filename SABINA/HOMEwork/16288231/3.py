count = 0
for n in range(1001,10000, 2):
    a1 = str(n)[0]
    a2 = str(n)[1]
    a3 = str(n)[2]
    a4 = str(n)[3]
    sum1 = int(a1) + int(a2)
    sum2 = int(a3) + int(a4)
    if sum1 < sum2:
        r = str(sum1) + str(sum2)
        if r == '616':
            count += 1
print(count)


