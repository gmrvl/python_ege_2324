a =[]
for n in range(1000,10000):
    s = str(n)
    a1 = int(s[0])
    a2 = int(s[1])
    a3 = int(s[2])
    a4 = int(s[3])
    summ1 = a1 + a2
    summ2 = a3 + a4
    if summ1 < summ2:
        r = str(summ1) + str(summ2)
        if r == '616':
            a.append(n)
print(a,len(a))
