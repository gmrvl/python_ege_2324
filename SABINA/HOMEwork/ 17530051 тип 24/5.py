f = open('5.txt').read()
k = 1
maxx = 0
i = 0
for i in range(1, len(f)):
    if f[i] == f[i-1] == 'R':
        k += 1
    if (f[i] == 'R') and f[i-1] != 'R':
        k += 0
    i = int(i) + 1
    maxx = max(maxx,k)
print(maxx)


