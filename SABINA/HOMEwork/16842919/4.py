f = open('4.txt')
cnt = 0
minn = 100000
maxx = -1
r = [int(i) for i in open('4.txt')]
for i in r:
    if r[-1]=='4' and r[-2] == '2':
        if r > maxx:
            maxx = r

fst = f.readline()
k = list(f)[:2]
for sec in f:
    for thd in k:
        fst, sec, thd  = int(fst), int(sec), int(thd)
        if (len(fst) == 3) or len(sec) == 3 or len(thd) == 3:
            if (fst + sec + thd) > maxx:
                cnt += 1
                if fst + sec + thd < minn:
                    minn = fst + sec + thd
        fst = sec
print(cnt, minn)

