f = [open('24.txt').readline()]
k = 0
c = 0
d = 0
maxx = -111
for i in range(len(f)):
    if f[i] != 'C' or f[i] != 'D':
        k += 1
        print(k)
        maxx = max(maxx, k)
    elif f[i] == 'C':
        k += 1
        c += 1
        print(c)
        maxx = max(maxx, k)
        if c > 2:
            f[i] == '*'
            f.split('*')
            # f.split(f[i])
            k = 1
            c = 1
            print(f)
    elif f[i] == 'D':
        k += 1
        d += 1
        maxx = max(maxx, k)
        if d > 2:
            f[i] == '*'
            f.split('*')
            #f.split(f[i])
            print(f)
            k = 1
            d = 1
#print(f)
maxx = max(maxx,k)
#print(maxx)