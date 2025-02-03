f = open('24_demo.txt').readline()
f = f.replace('XYZ', '*')
k = 3
maxx = 0
for i in range(len(f)):
    if f[i] == '*':
        k += 3
    else:
        if f[i-1] == '*':
            if f[i] == 'X':
                k += 1
            elif f[i:i+2] == 'XY':
                k += 2
        maxx = max(k, maxx)
        k = 0
print(maxx)
