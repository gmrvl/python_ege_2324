f = [int(i) for i in open('1_17.txt')]
maxx = -1
maxsum = -1
cnt = 0
for i in f:
    if 10 <= i <= 99:
        maxx = max(maxx,int(i))

f = open('1_17.txt')
fst = f.readline()
for sec in f:
    if 10 <= int(sec) <= 99 or 10 <= int(fst) <= 99:
        if (int(sec) + int(fst)) % maxx == 0:
            maxsum = max(maxsum,int(sec) + int(fst))
            cnt += 1
    fst = sec
print(cnt, maxsum)