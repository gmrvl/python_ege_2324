f = open('8.txt')
cnt = 0
maxx = -20000
fst = f.readline()
for sec in f:
    fst, sec = int(fst), int(sec)
    if ((fst % 18) + (sec % 5)) == min(fst,sec):
        cnt += 1
        maxx = max(maxx, fst + sec)
    fst = sec
print(cnt,maxx)