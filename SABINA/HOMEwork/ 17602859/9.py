f = open('9.csv')
cnt = 0
for i in f:
    a = list(map(int, i.split(';')))
    if a.count(max(a)) == 1:
        if len(set(a)) <= 4:
            if max(a)/((sum(a)-max(a))/5) > 3:
                cnt += 1
print(cnt)
