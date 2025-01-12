f = [int(x) for x in  open('17.txt')]
r = []
for i in range(0, len(f)-1):
    for j  in range(i+1, len(f)):
        x,y = f[i],f[j]
        if (x-y) % 60 == 0:
            if x % 15 == 0 or y % 15 == 0:
                r.append(x+y)
print(len(r),max(r))

