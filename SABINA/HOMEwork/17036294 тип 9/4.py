cnt = 0
f = open('4.csv')
for i in f:
    s = list(map(int,i.split(';')))
    if len(set(s)) == 4:
        if ((sum(s)- sum(set(s)))/4) < (sum(s)/7):
            cnt += 1
print(cnt)