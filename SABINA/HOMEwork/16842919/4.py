cnt = 0
minn = 100000
maxx = -1
r = [int(i) for i in open('4.txt')]
for i in r:
    if i % 100 == 24:
        if i > maxx:  # maxx = max(i, maxx)
            maxx = i
f = open('4.txt')
fst = f.readline()
sec = f.readline()
for thd in f:
    a = [len(fst) - 1, len(sec) - 1, len(thd) - 1]  # костыль
    # fst, sec, thd = int(fst), int(sec), int(thd)
    if (a.count(3) == 1) and ((int(fst) + int(sec) + int(thd)) > maxx):
        cnt += 1
        if int(fst) + int(sec) + int(thd) < minn:
            print(minn)
            minn = int(fst) + int(sec) + int(thd)
    fst = sec
    sec = thd
print(cnt, minn)

