cnt = 0
f = open('9.csv')
for i in f:
    s = list(map(int,i.split(';')))
    s = sorted(s)
    if (sum(s)-min(s))/min(s) > 6:
        if (min(s)*max(s)) > (int(s[1])*int(s[2])):
            cnt += 1
print(cnt)


