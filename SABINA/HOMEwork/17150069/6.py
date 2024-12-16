f = open('6.csv')
cnt = 0
for i in f:
    s =  list(map(int,i.split(';')))
    if max(s) > (sum(s)-max(s)):
        cnt +=1
print(cnt)
