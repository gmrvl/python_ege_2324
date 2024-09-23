f = open('09 (1).csv')
count = 0
for i in f:
    a = list(map(int,i.split(';')))
    a = sorted(a)
    s = set(a)
    if len(a) == len(s):
        for k in range(0,len(a)):
            if a.count(a[k]) == 45:
                count += 1
print(count)