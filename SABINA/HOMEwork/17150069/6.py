f = open('6.csv')
cnt = 0
for i in f:
    a = sorted(list(map(int, i.split(';'))))
    if a[0] + a[1] > a[3] and a[0] + a[2] > a[3] and a[1] + a[2] > a[3]:
        cnt += 1
print(cnt)
