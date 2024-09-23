cnt = 0
f = open('15.csv')
for i in f:
    a = list(map(int, i.split(';')))
    a = sorted(a)
    if len(set(a)) == 4:
        for k in (0, 6):
            if ((4*a[k])/4) > (sum(a)-4*a[k])/3:
                cnt += 1
print(cnt)