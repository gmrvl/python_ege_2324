a = []
for i in range(1,100):
    n = i
    r = ''

    while n > 0:
        r = str(n%3) + str(r)
        n = n//3
    if (sum(map(int,r)))%3 == 0:
        r = '112'+(r[2:])
    if (sum(map(int,r)))%3 == 1:
        summ = sum(map(int,r))
        summ_tr = ''
        while summ > 0:
            summ_tr = str(summ % 3) + str(summ_tr)
            summ = summ // 3
        r = str(r) + str(summ_tr)
    r = int(r,3)
    if r > 702:
        a.append(r)
print(min(a))




