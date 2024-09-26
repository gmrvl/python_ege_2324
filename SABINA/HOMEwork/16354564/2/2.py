count = 0
f = open('09 (1)csv.csv')
for i in f:
    a = list(map(int, i.split(';')))
    s = list(set(a))
    if len(s) == 4:
        p = []
        for k in range(0, len(a)):
            if a.count(a[k]) > 1:
                p.append(a[k])
        p = list(set(p))
        if len(p) == 2:
            if sum(p) > (sum(s) - sum(p)):
                count += 1
print(count)


