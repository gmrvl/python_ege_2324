f = open('4.csv')
cnt = 0
for i in f:
    s = list(map(int, i.split(';')))
    if len(set(s)) == 4:
        for k in range(0, len(s)):
            if s.count(s[k]) == 4:
                sr1 = int(s[k])
                sr2 = (sum(s) - int(s[k])*4) / 3
                if sr1 > sr2:
                    cnt += 1
                    break
print(cnt)
