f = open('16.txt')
cnt = 0
maxx = -20000
fst = f.readline()
for sec in f:
    fst, sec = int(fst), int(sec)
    s1, s2 = str(fst),str(sec)
    if s1[-1] == s2[-1]:
        if fst % 3 == 0 or sec % 3 == 0:
            if ((fst**2) + (sec**2)) < (min(fst,sec)**2):
                cnt +=1
                maxx = max(maxx, fst + sec)
    fst = sec
print(cnt,maxx)