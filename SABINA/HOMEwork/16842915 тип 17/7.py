f = open('7.txt')
cnt = 0
maxx = -20000
fst = f.readline()
for sec in f:
    fst, sec = int(fst), int(sec)
    if fst % 3 == 0 or sec % 3 == 0:
        cnt +=1
        maxx = max(maxx, fst + sec)
    fst = sec
print(cnt,maxx)