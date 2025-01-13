f = open('09 (9).csv')
cnt = 0
for i in f:
    r = []
    s = list(map(int,i.split(';')))
    if (len(set(s)) != len(s)) and s.count(max(s)) == 1:
        for k in range(len(s)):
            if s.count(s[k]) > 1:
                r.append(s.count(s[k]) * int(s[k]))
    if sum(r) < max(s):
        cnt+=1
print(cnt)