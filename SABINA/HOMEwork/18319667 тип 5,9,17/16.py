f = open('16.txt')
maxx = -11
for ma in f:
    ma = int(ma)
    if ma % 100 == 17:
        maxx = max(ma,maxx)

f = open('16.txt')
maxsum = -111
cnt = 0
fst = f.readline()
sec = f.readline()
for thd in f:
    fst,sec,thd = int(fst),int(sec),int(thd)
    if (1000<=fst<=9999 and 1000<=sec<=9999) or (1000<=sec<=9999 and 1000<=thd<=9999) or (1000<=fst<=9999 and 1000<=thd<=9999):
        if (fst % 5 == 0) or (sec % 5 == 0) or (thd % 5 == 0):

            if (fst+sec+thd) > maxx:
                print(fst,sec,thd,maxx,fst+sec+thd)
                cnt +=1
                maxsum = max(maxsum,fst+sec+thd)
    fst = sec
    sec = thd
print(cnt,maxsum)
