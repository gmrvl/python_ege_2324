cnt = 0
summ = 0
f = open('4.csv')
for i in f:
    a = list(map(int, i.split(';')))
    if len(set(a)) != len(a):
        for k in range(0, len(a)):
            if a[k] > 1:
                summ = (a.count(a[k]) * int(a[k])) + summ
        if max(a) < summ:
            cnt += 1
print(cnt)
