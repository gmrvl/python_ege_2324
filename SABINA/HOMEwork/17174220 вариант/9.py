f = open('09 (9).csv')
cnt = 0
r = [[],[],[],[],[],[]]
for i in f:
    s = list(map(int, i.split(';')))
    for j in range(6):
        r[j].append(s[j])
f = open('09 (9).csv')
for i in f:
    s = list(map(int, i.split(';')))
    interes = 0
    for j in range(6):
        if s.count(s[j]) == 1 and r[j].count(s[j]) < 170:
            interes += 1
    if interes >= 4:
        cnt += 1
print(cnt)


