k = []
for i in range(1000,10000):
    s = str(i)
    a1 = int(s[0])
    a2 = int(s[1])
    a3 = int(s[2])
    a4 = int(s[3])
    summ1 = a1 + a2
    summ2 = a2 + a3
    summ3 = a3 + a4
    k = [summ1,summ2,summ3]
    k = sorted(k)
    r = str(k[1])+str(k[2])
#    print(r)

    if r == '210':
        print(i)
