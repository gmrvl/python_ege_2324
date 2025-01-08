f = open('09 (9).csv')
cnt = 0
r = []
for i in f:
    s = list(map(int, i.split(';')))
    for k in range(0, len(s)):
        if s.count(s[k]) == 1:
            r.append(k)
for l in r:
    if s.count(r[l]) < 170:
        cnt+=1
print(cnt)


