f = open('demo_2025_9.csv')
count = 0
for s in f:
    a = sorted(list(map(int, s.split(';'))))
    if a[0] == a[1] == a[2] and a[2] != a[3] and a[3] != a[4] and a[4] != a[5]:
        if (a[0]*3)**2 > (a[3] + a[4] + a[5])**2:
            count += 1
    if a[0] != a[1] and a[1] == a[2] == a[3] and a[3] != a[4] and a[4] != a[5]:
        if (a[1]*3)**2 > (a[0] + a[4] + a[5])**2:
            count += 1
    if a[0] != a[1] and a[1] != a[2] and a[2] == a[3] == a[4] and a[4] != a[5]:
        if (a[2]*3)**2 > (a[0] + a[1] + a[5])**2:
            count += 1
    if a[0] != a[1] and a[1] != a[2] and a[2] != a[3] and a[3] == a[4] == a[5]:
        if (a[3]*3)**2 > (a[0] + a[1] + a[2])**2:
            count += 1
print(count)

