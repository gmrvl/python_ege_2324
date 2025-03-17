f = open('9_58322.csv')
cnt = 0
for i in f:
    s = list(map(int,i.split(';')))
    c = sorted(s)
    print(c)
    if c[3]-c[2] == c[2]-c[1] == c[1]-c[0]:
        print('1')
        if s[0] == max(s) and (s[0])**2 > s[1] * s[2] * s[3]:
            cnt += 1
        if s[1] == max(s) and (s[1]) ** 2 > s[0] * s[2] * s[3]:
            cnt += 1
        if s[2] == max(s) and (s[2]) ** 2 > s[0] * s[1] * s[3]:
            cnt += 1
        if s[3] == max(s) and (s[3]) ** 2 > s[0] * s[2] * s[1]:
            cnt += 1

print(cnt)
