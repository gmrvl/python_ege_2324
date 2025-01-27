f = open('17.txt')
r = []
naim = []
for i in f:
    r.append(i)
p = 0
for k in range(0,len(r)):
    p = int(r[k])
    if (p % 10 == 3) and (len(str(p)) == 3):
        naim.append(p)

f = open('17.txt')
fst = f.readline()
cnt = 0
minn = 1000000
for sec in f:
    fst,sec = int(fst),int(sec)
    if (len(str(fst))== 4) or ((len(str(sec)))== 4):
        if ((sec**2)+(fst**2)) % min(naim) == 0:
            cnt+=1
    fst = sec
    minn = min(minn,(fst**2)+(sec*2))
print(cnt,minn)

