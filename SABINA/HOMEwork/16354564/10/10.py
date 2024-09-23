cnt = 0
f = open('10.csv')
for i in f:
    a = list(map(int,i.split(';')))
    if (max(a)+ min(a))**2 > (sum(a)-min(a)-max(a))**2:
        cnt +=1
print(cnt)