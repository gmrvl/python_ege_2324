f = open('17.txt')
cnt = 0
f = f.readline()
maxx = -100
for sec in f:
    fst,sec = int(fst),int(sec)
    if (len(fst)== 4) or (len(sec))== 4):
        if ((sec**2)+(fst**2)) %