f = open('11.txt')
cnt = 0
maxx = -20000
fst = f.readline()
for sec in f:
    strfst, strsec = str(fst),str(sec)
    fst, sec = int(fst), int(sec)
    if strfst[-1] == strsec[-2]:
        if fst % 7 == 0 or sec % 7 == 0:
            if ((fst**2)+ (sec**2)) <= ((int(min(strsec, strfst))) ** 2):
                cnt +=1
                maxx = max(maxx, fst + sec)
        fst = sec
    elif strsec[-1] == strfst[-2]:
        if fst % 7 == 0 or sec % 7 == 0:
            if ((fst**2)+ (sec**2)) <= ((int(min(strsec, strfst))) ** 2):
                cnt +=1
                maxx = max(maxx, fst + sec)
        fst = sec
    else:
        break
print(cnt,maxx)