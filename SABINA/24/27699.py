f = open('27699.txt').readline()
k = m = 0
for i in range(len(f)):
    if (f[i] == 'L' and k%3 == 0) or (f[i] == 'D' and k%3 == 1) or (f[i] == 'R' and k%3 == 2):
        k += 1
    elif f[i] == 'L':
        m = max(m, k)
        k = 1
    else:
        m = max(m, k)
        k = 0
print(m)