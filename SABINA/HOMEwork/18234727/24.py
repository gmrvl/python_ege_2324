s = open('24.txt')
cnt = 0
maxx = -11111111111
while i > 0:
    for i in s:
        p = []
        for k in i:
            if k != 'E':
                if p.count('A') >= 3:
                    cnt += 1
                    maxx = max(cnt, maxx)
            else:
                cnt += 0
                maxx = max(cnt,maxx)
            i = i[1:]
print(maxx)
