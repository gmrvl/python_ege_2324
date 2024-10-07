cnt=0
f = open('09 (1).csv')
for i in f:
    a = list(map(int, i.split(';')))
    if len(set(a)) == len(a):
        if (max(a)+min(a))/2 < (sum(a)-min(a)-max(a))/4:
            cnt+=1
print(cnt)