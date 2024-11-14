f = [int(x) for x in open('1.txt')]
cnt = 0
maxx = -1

for i in range(0, len(f) - 1):
    for j in range(i + 1, len(f)):
        if (f[i] + f[j]) % 2 == 1 and (f[i] * f[j]) % 5 == 0:
            cnt += 1
            if (f[i] + f[j]) > maxx:
                maxx = f[i] + f[j]
print(cnt, maxx)
