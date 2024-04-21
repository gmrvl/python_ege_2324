count = 0
for i in range(1000,10000):
    s = str(i)
    a1 = s[0]
    a2 = s[1]
    a3 = s[2]
    a4 = s[3]
    # дописать условие
    sum1 = int(a1) + int(a2)
    sum2 = int(a3) + int(a4)
    if sum1 < sum2:
        n = str(sum1) + str(sum2)
    else:
        n = str(sum2) + str(sum1)
    if n == '616':
        count += 1
print(count)