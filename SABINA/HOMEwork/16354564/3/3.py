count = 0
f = open('107_9csv.csv')
for i in f:
    a = list(map(int,i.split(';')))
    a = sorted(a)
    if a[0]+a[1]>a[2] and a[1]+a[2]<a[3] :
        count+=1
print(count)        