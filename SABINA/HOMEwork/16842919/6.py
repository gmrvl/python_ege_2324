f = [int(x) for x in open('6.txt')]
krat = []
R = []
for k in f:
    if k % 32 == 0:
        krat.append(k)
for i in range(0, len(f)-1):
    for j in range(i+1, len(f)):
        x, y = f[i], f[j]
        if (x < 0) or (y < 0):
            if x + y < len(krat):
                R.append(x+y)
print(len(R), max(R))
