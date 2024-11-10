f  = open('3.txt')
cnt = 0
maxx = -1
fst = f.readline()
for sec in f:
    fst , sec = int(fst), int(sec)
    if (abs(fst - sec) % 60 == 0) and \
            (fst % 15 == 0) or (sec % 15 == 0):
        cnt += 0
        if abs(fst - sec) > maxx:
            maxx = abs(fst - sec)
    fst = sec
print(cnt, maxx)