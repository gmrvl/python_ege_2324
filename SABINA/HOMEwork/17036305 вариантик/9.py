cnt = 0
f = open('1_9.csv')
for i in f:
    s = list(map(int, i.split(';')))
    if max(s) < (sum(s)-max(s)):
        # for k in range(0, len(s)-1):
        #     for l in range(k+1, len(s)):
        #         if (sum(s)/2) == s[k]+s[l]:
        #             cnt += 1
        #             break
        s = sorted(s)
        if s[0] + s[3] == s[1] + s[2]:
            cnt += 1
print(cnt)
