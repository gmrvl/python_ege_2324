cnt = 0
f = open('2.csv')
for i in f:
    s = list(map(int, i.split(';')))
    for k in range(len(s)):
        if len(set(s)) == 4:
            if s.count(s[k]) < 3:
                if sum(s)-sum(set(s)) < sum(set(s)):
                    cnt += 1
print(cnt)