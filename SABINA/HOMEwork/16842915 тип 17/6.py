f = open('6.txt')
cnt = 0
maxx = - 100
fst = f.readline()
sec = f.readline()
for thd in f:
    fst, sec, thd = int(fst), int(sec), int(thd)
    if max(fst, sec, thd) == fst:
        if fst ** 2 == (sec ** 2) + (thd ** 2):
            cnt += 1
            maxx = max((fst + sec + thd), maxx)
    elif max(fst, sec, thd) == sec:
        if sec ** 2 == (fst ** 2) + (thd ** 2):
            cnt += 1
            maxx = max((fst + sec + thd), maxx)
    elif max(fst, sec, thd) == thd:
        if thd ** 2 == (sec ** 2) + (fst ** 2):
            cnt += 1
            maxx = max((fst + sec + thd), maxx)
    '''
    a = sorted([fst, sec, trd])
    if (a[0])**2 + (a[1])**2 == (a[2])**2:
        cnt += 1
        maxx = max((fst + sec + thd), maxx)
    '''
    fst, sec = sec, thd
print(cnt, maxx)
