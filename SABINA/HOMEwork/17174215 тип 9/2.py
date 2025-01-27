cnt = 0
f = open('2.csv')
sr = 0
for i in f:
    a = list(map(int,i.split(';')))
    if len(set(a)) == 5:
        for k in range(0,len(a)):
            if a.count(a[k]) == 3:
                sr = (sum(a) - (a.count(a[k]) * int(a[k]))) / 4
                if a[k] >= sr:
                    cnt+=1
                    break
print(cnt)