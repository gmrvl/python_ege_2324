cnt = 0
f = open('1.csv')
for i in f:
    summ = 0
    a = list(map(int, i.split(';')))
    if len(set(a)) != len(a):
        if a.count(max(a)) == 1:
            for k in range(0, len(a)):
                if a.count(a[k]) > 1:
                    summ = int(a[k]) + summ
            if max(a) < summ:
                cnt += 1
print(cnt)

