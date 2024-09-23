count = 0
f = open('09сым.csv')
for i in f:
    a = list(map(int,i.split(';')))
    a = sorted(a)
    if  a[0]*a[1] + a[0]*a[2]  > a[1]*a[2] :
        count+=1
print(count)