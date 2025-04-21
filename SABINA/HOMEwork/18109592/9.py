f = open('09.csv')
for i in f:
    s = list(map(int,i.split(';')))
    for k in range(len(s)):
        if s.count(s[k]) == 1:
            if s[k] == s[0]:
                if int(s[k+1]) > int(s[k]):
                    cnt += 1
