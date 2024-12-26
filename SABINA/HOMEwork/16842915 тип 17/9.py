f = open('9.txt')
cnt = 0
min21 = 1000000
for delit in f:
    delit = int(delit)
    if delit % 21 == 0 and delit < min21:
        min21 = delit

f = open('9.txt')
maxx = -20000
fst = f.readline()
for sec in f:
    fst, sec = int(fst), int(sec)
    if fst % min21 == 0 or sec % min21 == 0:
        if (fst + sec) % 7 == 0:
            cnt +=1
            maxx = max(maxx, fst + sec)
    fst = sec
print(cnt,maxx)