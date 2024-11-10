f  = [int(x) for x in open('3.txt')]
cnt = 0
maxx = -1

for i in range(0, len(f)-1):
    for j in range(i+1, len(f)):
        fst, sec = f[i], f[j]
        if (abs(fst - sec) % 36 == 0) and \
                ((fst % 13 == 0) or (sec % 13 == 0)):
            cnt += 1
            if abs(fst - sec) > maxx:
                maxx = abs(fst - sec)
print(cnt, maxx)