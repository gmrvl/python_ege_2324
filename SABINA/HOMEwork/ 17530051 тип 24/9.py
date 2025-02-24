f = open('9.txt').read()
k = 0
minn = 1000000
f = f[24:]
print(f)
while len(f) > 0:
    for i in range(1,len(f)):
        if f[i-1] == 'T':
            k+= 1
            if k == 100:
                minn = min(minn,k)
        else: