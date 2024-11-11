f = open('8.txt')
cnt = 0
maxx = -1
fir = f.readline()
for sec in f:
    fir, sec = int(fir), int(sec)
    if abs(fir-sec) % 60 == 0:
        cnt += 1
        if abs(fir-sec) > maxx:
            maxx = abs(fir-sec)
print(cnt, maxx)
