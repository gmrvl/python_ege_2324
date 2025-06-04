f = open('11.csv')
cnt = 0
for i in f:
    s = list(map(int, i.split(';')))
    if len(set(s)) != len(s):
        for k in range(len(s)):
            if s.count(s[k]) == 3:
                if s[k] >= (sum(s)-s[k]*3)/3:
                    cnt+=1
                    break
print(cnt)