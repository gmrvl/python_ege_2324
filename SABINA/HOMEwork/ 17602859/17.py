m  = [int(x) for x in open('17.txt')]
r = []
for i in range(0, len(m)-1):
    for j in range(i+1,len(m)):
        x,y = m[i],m[j]
        if (x-y) % 80 == 0:
            r.append(x-y)
print(len(r),max(r))