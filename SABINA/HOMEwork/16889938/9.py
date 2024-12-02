f = open('9.csv')
cnt = 0
for i in f:
    s = list(map(int, i.split(';')))
    if len(set(s)) == len(s):
        if 2*(max(s)+min(s)) <= (sum(s)-max(s)-min(s)):
            cnt += 1
print(cnt)
