f = open('09 (1)csv.csv')
cnt = 0
for s in f:
    a = list(map(int, s.split(';')))
    if len(set(a)) != len(a):
        if a.count(max(a)) == 1:
            suma = 0
            for i in range(0, len(a)):
                if a.count(a[i]) > 1:
                    suma += a[i]
            if suma < max(a):
                cnt += 1
print(cnt)