f = open('09 (4).csv')
cnt = 0
for i in f:
    a = list(map(int,i.split(';')))
    s = str(set(a))
    for k in range(0,len(a)):
        if len(set(a)) != len(a) and a.count(a[k]) == 1:
            if a[k] > a[(k-1)>-1] or a[k] > a[(k+1)<7]:
                if len(set(a)) > 3:
                    cnt += 1
print(cnt)
