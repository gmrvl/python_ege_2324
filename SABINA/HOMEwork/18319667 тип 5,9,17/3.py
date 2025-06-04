maxx = -111
for n in range(1,50):
    ost = bin(n % 4)[2:]
    i = bin(n)[2:]
    r = str(i) + str(ost)
    r = int(r,2)
    maxx = max(maxx,r)
    print(r,maxx)
print(maxx)