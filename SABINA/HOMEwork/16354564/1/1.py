count = 0
f = open('09.csv')
for i in f:
    a = list(map(int,i.split(';')))
    a = sorted(a)
    s = set(a)
    if len(a) == len(s):
        if (a[0]+a[5])/2 < (a[1]+a[2]+a[3]+a[4])/4:
            count+=1
print(count)