count = 0
for i in range(1111, 10000, 2):
    nech = '13579'
    s = str(i)
    flag = True
    for j in s:
        if not (j in nech):
            flag = False
            break
    if not flag:
        continue
    a1, a2, a3, a4 = int(s[0]), int(s[1]), int(s[2]), int(s[3])
    summ1 = a1 + a2
    summ2 = a3 + a4
    if summ1 < summ2:
        n = str(summ1) + str(summ2)
    else:
        n = str(summ2) + str(summ1)
    if n == '616':
        count += 1
print(count)