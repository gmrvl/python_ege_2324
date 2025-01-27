cnt = 0
r = 0
for n in range(1000, 10000):
    s = str(n)
    a1 = s[0]
    a2 = s[1]
    a3 = s[2]
    a4 = s[3]
    summ1 = int(a1) + int(a2)
    summ2 = int(a3) + int(a4)
    if summ1 < summ2:
        r = str(summ1) + str(summ2)
    if int(r) == 616:
        cnt += 1
print(cnt)