cnt = 0
f = open('3.csv')
for i in f:
    a = list(map(int,i.split(';')))
    a = sorted(a)
#    print(a)
    if int(a[1]) + int(a[2]) < int(a[3]):
        cnt += 1
print(cnt)