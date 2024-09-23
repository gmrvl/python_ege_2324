cnt = 0
f = open('14.csv')
for i in f:
    a = list(map(int, i.split(';')))
    a = sorted(a)
    if len(set(a)) == 5:
        for k in (0, 5):
            if (sum(a)-2*a[k])/4 < 2*a[k]:
                cnt += 1
print(cnt)