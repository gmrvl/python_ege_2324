f = open('3.txt').readline()
cnt = 0
maxx = 0
for i in range(1, len(f)):
    if f[i] != f[i-1]:
        cnt +=1
        maxx = max(cnt, maxx)
    else:
        maxx = max(cnt,maxx)
        cnt = 1
print(maxx)
