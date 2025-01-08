cnt = 0
minn = 100000
maxx = -1
r = [int(i) for i in open('12.txt')]
for i in r:
    if i % 100 == 13:
        if i > maxx:  # maxx = max(i, maxx)
            maxx = i
f = open('12.txt')
fst = f.readline()
sec = f.readline()
for thd in f:
    a = [99<abs(int(fst))<1000, 99<abs(int(sec))<1000, 99<abs(int(thd))<1000]
    if (a.count(True) == 2) and ((int(fst) + int(sec) + int(thd)) < maxx):
        cnt += 1
        print(int(fst), int(sec), int(thd))
        if int(fst) + int(sec) + int(thd) < minn:
            minn = int(fst) + int(sec) + int(thd)
    fst = sec
    sec = thd
print(cnt, minn)