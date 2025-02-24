f = open('2.txt')
minG = 20000
minGs = ''
for s in f:
    if s.count('G') < minG:
        minG = s.count('G')
        minGs = s
a = [0]*100
for i in minGs:
    a[ord(i)] += 1
maxx = max(a)
for i in range(65, 100):
    if a[i] == maxx:
        print(a[i], chr(i))


