f = open('9.csv')
cnt = 0
for i in f:
    s = list(map(int,i.split(';')))
    if len(set(s)) == 5:
        for k in range(len(s)):
            if s.count(s[k]) == 2:
                cnt += 1
                break
print(cnt)