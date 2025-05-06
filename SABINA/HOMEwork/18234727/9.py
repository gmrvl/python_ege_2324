f = open('9.csv')
cnt = 0
for i in f:
    c = []
    nc = []
    s = list(map(int,i.split(';')))

    if len(set(s)) != len(s):
        for k in range(len(s)):
            if s[k] % 2 == 0:
                c.append(s[k])
            else:
                nc.append(s[k])
        if len(c) > len(nc) and sum(c)<sum(nc):
            cnt += 1
print(cnt)