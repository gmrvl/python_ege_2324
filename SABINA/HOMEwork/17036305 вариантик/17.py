f = open('17.txt')
cnt = 0
maxx = -1000
fst = f.readline()
for sec in f:
    fst,sec = int(fst),int(sec)
    if fst % 5 == 0 or sec % 5 == 0 and (fst + sec) % 7 == 0:
        cnt +=1
        if fst + sec > maxx:
            maxx = fst + sec
        fst = sec
print(cnt, maxx)