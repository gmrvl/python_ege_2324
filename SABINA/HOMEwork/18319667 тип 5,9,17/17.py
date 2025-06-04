f = [int(x) for x in open('17.txt')]
summ = []
cnt = 0
maxsum = -111
for i in range(0,len(f)-1):
    for j in range(i,len(f)):
        x,y = f[i],f[j]
        if (x % 160) != (y % 160):
            if (x % 7 == 0) or (x % 7 == 0) or (x % 7 == 0):
                summ.append(x+y)
print(len(summ),max(summ))
