cnt = 0
f = open('2.csv')
for i in f:
    s = list(map(int, i.split(';')))
    if len(set(s)) == 4:
        f = True
        for k in range(len(s)):
            if s.count(s[k]) >= 3:
                f = False
                break
        if f == True and (sum(s) - sum(set(s)) < sum(set(s)) - (sum(s) - sum(set(s)))):
            cnt += 1

print(cnt)
