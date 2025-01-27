cnt = 0
summ = 0
f = open('1.csv')
for i in f:
    a = list(map(int, i.split(';')))
    if len(set(a)) != len(a):
        if a.count(max(a)) == 1:
            for k in range(0,len(a)):
                if a[k] > 1:
                    summ = (a.count(a[k])*int(a[k])) + summ
            if max(a) < summ:
                cnt+=1
print(cnt)

