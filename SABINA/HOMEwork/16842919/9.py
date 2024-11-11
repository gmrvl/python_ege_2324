f = [int(x) for x in open('9.txt')]
R = []
minn = 100000
for m in f:
    if m < minn:
        minn = m
for i in range(0, len(f)-1):
    for j in range(i+1, len(f)):
        x, y = f[i], f[j]
        if ((x % 18) + (y % 18)) == minn:
                R.append(x + y)
print(len(R), max(R))

