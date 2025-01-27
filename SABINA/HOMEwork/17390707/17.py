
maxx = -100
cnt = 0
r = [int(i) for i in open('17.txt')]
for i in r:
    if i % 1000 == 321:
        maxx = max(i,maxx)
f = open('17.txt')
fst = f.readline()
sec = f.readline()
for thd in f:
    fst,sec,thd = int(fst),int(sec),int(thd)
    if (fst % 5 == 0) or (sec % 5 == 0) or (thd % 5 == 0):
        if (fst+sec+thd) > maxx:
            cnt += 1
            maxx = max(fst+sec+thd,maxx)
print(cnt, maxx)