cnt = 0
f = open('12.csv')
for i in f:
    a = list(map(int, i.split(';')))
    a = sorted(a)
    if len(set(a)) == 4:
        for k in (0, 5):
            if a[k] > (sum(a) - 3 * a[k]) / 3:
                cnt += 1
print(cnt)