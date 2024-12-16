cnt = 0
f = open('5.csv')
for i in f:
    s = list(map(int, i.split(';')))
    if s.count(min(s)) == 1 and len(set(s)) < 6:
        if (max(s) / ((sum(s)-max(s))/5)) > 3:
            cnt += 1
print(cnt)
