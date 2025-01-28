cnt = 0
for i in range(1001, 10000, 1):
    n = 0
    s = str(i)
    a1 = s[0]
    a2 = s[1]
    a3 = s[2]
    a4 = s[3]
    summ1 = int(a1)+int(a2)
    summ2 = int(a3)+int(a4)
    if summ1 < summ2:
        n = str(summ1)+str(summ2)
    if n == '414':
        cnt+=1
print(cnt)