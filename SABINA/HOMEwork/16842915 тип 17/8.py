f = open('8.txt')
cnt = 0
maxx = -20000
fst = f.readline()
for sec in f:
    fst, sec = int(fst), int(sec)
    if fst % 5 == 0 or sec % 5 == 0:
        if (fst + sec) % 7 == 0:
            cnt +=1
            maxx = max(maxx, fst + sec)
    fst = sec
print(cnt,maxx)