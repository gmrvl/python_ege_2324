f = open('8.txt').read()
a = 'ABCDEF'
k = 0
maxx = 0
r = []
cnt = 0
for i in range(1, len(f)):
    for l in range(1, len(a)):
        if f[i-1] == a[l-1]:
            r.append(f[i-1])
            if k > 3 and r.count('CD') <= 140:
                maxx = max(maxx, k)
        if f[i] != a[l]:
            k += 0
            if k > 3 and r.count('CD') <= 140:
                maxx = max(maxx, k)
maxx = max(maxx, k)
print(maxx)