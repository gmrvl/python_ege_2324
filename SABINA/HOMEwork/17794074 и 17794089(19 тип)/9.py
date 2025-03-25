f = open('9_58322.csv')
cnt = 0
for i in f:
    s = list(map(int, i.split(';')))
    c = sorted(s)
    if ((c[3]-c[2] == c[2]-c[1]) and (c[2]-c[1] == c[1]-c[0])) or ((c[3])**2 > c[1] * c[2] * c[0]):
            cnt += 1
print(cnt)
