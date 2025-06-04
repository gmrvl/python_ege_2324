f = open('13.csv')
cnt = 0
for i in f:
    s = list(map(int,i.split(';')))
    if len(set(s)) == 4:
        for k in range(len(s)-1):
            for p in range(1,len(s)):
                if (s.count(s[k]) == 2) and (s.count(s[p]) == 2) and (s[k] != s[p]):
                    if (s[k]+s[p]) < (sum(s)-2*s[k]-2*s[p]):
                        cnt+=1
                        break
print(cnt)
