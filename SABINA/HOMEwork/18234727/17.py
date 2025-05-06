f = open('17.txt')
minn = 10000000
maxx = -111111111
for i in f:
    i = int(i)
    maxx = max(i,maxx)
    minn = min(i,minn)
#print(minn,maxx)

maxsum = -1000000
f = open('17.txt')
cnt = 0
fst = f.readline()
for sec in f:
    fst,sec = int(fst),int(sec)
    if ((fst % 3 == minn % 3) or (sec % 3 == minn % 3))or((fst % 3 == minn % 3) and (sec % 3 == minn % 3)):
        cnt += 1
        maxsum = max(maxsum,fst+sec)
    if ((fst % 7 == maxx % 7) or (sec % 7 == maxx % 7))or((fst % 7 == maxx % 7) and (sec % 7 == maxx % 7)):
        cnt += 1
        maxsum = max(maxsum, fst + sec)
fst = sec
print(cnt,maxsum)