count = 0
f = open('5.csv')
for i in f:
    a = list(map(int, i.split(';')))
    a = sorted(a)
    s = set(a)
    if len(a) == len(s) and a[3] < a[0]+a[1]+a[2]:
        count+=1
print(count)