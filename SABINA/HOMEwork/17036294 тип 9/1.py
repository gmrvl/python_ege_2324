cnt = 0
f = open('1.csv')
for i in f:
    s = list(map(int, i.split(';')))
    for k in range(len(s)):
        if s.count(s[k]) == 3:
            if ((sum(s) - 3*(int(s[k])))/3) < s[k]:
                cnt += 1
print(cnt)