f = open('13.txt')
cnt = 0
maxx = -20000
fst = f.readline()
for sec in f:
    fst, sec = int(fst), int(sec)
    if fst % 10 == 7 or sec % 10 == 7:
        if ((fst**2) + (sec**2)) < (min(fst,sec)**2):
            cnt +=1
            maxx = max(maxx, fst + sec)
    fst = sec
print(cnt,maxx)