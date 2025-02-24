f = open('1.txt').readline()
cnt = 0
maxx = 0
for i in f:
    if ('AOC' in f) or ('AOD' in f) or ('AOF' in f) or ('OAC' in f) or ('OAD' in f) or ('OAF' in f) or \
        ('AAC' in f) or ('AAD' in f) or ('AAF' in f) or ('OOC' in f) or ('OOD' in f) or ('OOF' in f):
            cnt +=1
            maxx = max(cnt, maxx)
    else:
        maxx = max(cnt,maxx)
        cnt = 1
maxx = max(maxx,cnt)
print(maxx)