cnt = 0
f = open('3.csv')
for i in f:
    s = list(map(int, i.split(';')))
    if len(set(s)) == len(s):
        if ((sum(s)-min(s)-max(s))/4) > ((min(s)+max(s))/2):
            cnt+=1
print(cnt)
