f = [int(x) for x in open('7.txt')]
R = []
nc = []
for n in f:
    if n % 2 ==1:
        nc.append(n)
for i in range(0, len(f)-1):
    for j in range(i +1 , len(f)):
        x , y = f[i] , f[j]
        if (x % 5 == 0) and ( y < (sum(nc)/len(nc))):
            R.append(x+y)
print(len(R), max(R))