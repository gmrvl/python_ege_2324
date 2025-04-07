f = open('17.txt')
minn = 1000000
maxx = -1
cnt = 0
for k in f:
    if 99 < int(k) < 1000 and (int(k) % 10 == 3):
        minn = min(minn,int(k))
print(minn)
f = open('17.txt')
fst = f.readline()
for sec in f:
    fst, sec = int(fst), int(sec)
    if len(str(fst)) == 4 and len(str(sec)) != 4 or :
        if ((fst)**2 + (sec)**2) % minn == 0:
            cnt += 1
            maxx = max(maxx,((fst)**2 + (sec)**2))
print(cnt,maxx)