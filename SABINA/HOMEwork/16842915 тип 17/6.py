f = open('6.txt')
cnt = 0
maxx = - 100
fst = f.readline()
sec = f.readline()
for thd in f:
    fst,sec,thd = int(fst),int(sec),int(thd)
    if max(fst,sec,thd) == fst :
        if fst**2 == (sec**2) + (thd**2):
            cnt +=1
    elif max(fst,sec,thd) == sec :
        if sec**2 == (fst**2) + (thd**2):
            cnt +=1
    elif max(fst,sec,thd) == thd :
        if thd**2 == (sec**2) + (fst**2):
            cnt +=1
    maxx = max((fst+sec+thd), maxx)
print(cnt,maxx)
