f = open('6.txt').read()
maxx = 0
k = 1
for p in 'AO':
    for l in 'CDF':
        for c in 'CDF':
            a = str(c)+ str(k) + str(p)

            for i in range(0, len(f)-1):
                if f[i] == f[i + 1] == a:
                    k += 1
                if (f[i] == a) and f[i + 1] != a:
                    k += 0

                maxx = max(maxx,k)
print(maxx)