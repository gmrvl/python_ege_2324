f = open('18.txt')
cnt = 0
maxx = -20000
fst = f.readline()
for sec in f:
    fst, sec = int(fst), int(sec)
    minn = str(min(fst,sec))
    if minn[-1] == 5:
        if ((fst**2) + (sec**2)) < (minn**2):
            cnt +=1
            maxx = max(maxx, fst + sec)
    fst = sec
print(cnt,maxx)