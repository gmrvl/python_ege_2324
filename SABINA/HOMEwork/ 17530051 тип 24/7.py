f = open('7.txt').read()
k = 1
maxx = 0
for i in range(1, len(f)):
    if int(f[i-1]) == (int(f[i]) + 1):
        k +=1
    if int(f[i-1]) != (int(f[i]) + 1):
        k += 0
    maxx = max(maxx, k)
print(maxx)