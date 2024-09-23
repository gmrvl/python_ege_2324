cnt = 0
f = open('11.csv')
for i in f:
    a = list(map(int, i.split(';')))
    if len(set(a)) != len(a) and max(a) == 1 and (max(a) / ((sum(a) - max(a))/5))  > 3 :
        cnt += 1
print(cnt)
        