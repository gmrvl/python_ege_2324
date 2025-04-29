f  = [int(x) for x in open('17.txt')]
maxx = -1000
r = []
for i in range(0,len(f)-1):
    for j in range(i + 1,len(f)):
        x,y = f[i],f[j]
        if (x+y) % 126 == 0:
            r.append(x+y)
print(len(r),max(r))
