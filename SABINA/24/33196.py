f = open('24.txt').readline()
a = ''
for i in range(len(f)):
    if f[i] == 'A':
        a += f[i+1]

maxx = 0
res = 0
for i in a:
    if a.count(i)> maxx:
        maxx = a.count(i)
        res = i
print(res)

