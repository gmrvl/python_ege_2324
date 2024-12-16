f =[int(x) for x in open('4.txt')]
r = []
for i in range(0,len(f)-1):
    for j in range(i+1,len(f)):
        x,y = f[i],f[j]
        if (x + y) % 80 == 0:
            if x % 50 == 0 or y % 50 == 0:
                r.append(x+y)
print(len(r),max(r))
            