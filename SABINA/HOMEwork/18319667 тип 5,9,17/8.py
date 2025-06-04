f = open('8.csv')
cnt = 0
for i in f:
    s = list(map(int, i.split(';')))
    s = sorted(s)
    print(s)
    if (s[0]*s[1])+(s[0]*s[2]) > s[1]*s[2]:
        cnt += 1
print(cnt)