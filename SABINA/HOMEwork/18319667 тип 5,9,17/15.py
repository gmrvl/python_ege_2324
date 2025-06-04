f = open('15.txt')
minn = 100000000
maxx = -1
for mi in f:
    minn = min(minn,int(mi))
for ma in f:
    maxx = max(maxx,int(ma))

f = open('15.txt')
cnt = 0
maxsum = -111
fst = f.readline()
for sec in f:
    fst,sec = int(fst),int(sec)
    if (fst % 3 == minn % 3) or (sec % 3 == minn % 3):
        cnt += 1
        maxsum = max(maxsum,fst+sec)
    if (fst % 7 == maxx % 7) or (sec % 7 == maxx % 7):
        cnt += 1
        maxsum = max(maxsum, fst + sec)
    fst = sec
print(cnt,maxsum)
