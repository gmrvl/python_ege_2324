f = open('14.csv')
cnt = 0
for i in f:
    s = list(map(int,i.split(';')))
    if 2 <= len(set(s)) <= 4:
        nepov = []
        for k in range(len(s)):
            if s.count(s[k]) == 1:
                nepov.append(s[k])
        else:
            if len(nepov) != 0:
                sr_nepov = sum(nepov)/len(nepov)
                sr_pov = (sum(s)-sum(nepov))/(len(s)-len(nepov))
                if sr_pov < sr_nepov:
                    cnt += 1
print(cnt)