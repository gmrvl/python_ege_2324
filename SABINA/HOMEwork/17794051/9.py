f = open('9.csv')
cnt = 0
for i in f:
    s = list(map(int,i.split(';')))
    c = sorted(s)
    if ((c[3]-c[2] == c[2] - c[1]) and (c[2]-c[1] == c[1] - c[0])) or ((c[3])**2 > c[0]*c[1]*c[2]):
        cnt += 1
print(cnt)




'''f = open('9.csv')
cnt = 0
for i in f:
    s = list(map(int,i.split(';')))
    s = sorted(s)
    for k in range(len(s)):
        if s[k] != max(s) and s[k] != min(s):
            if ((max(s))**2) > ((sum(s)-max(s)-min(s)-int(s[k]))*int(s[k])*min(s)):
#                print(int(s[3]) - int(s[2]), int(s[2]) - int(s[1]), int(s[1]) - int(s[0]))
                if (int(s[3])-int(s[2])) == (int(s[2])-int(s[1])) and int(s[2])-int(s[1]) == (int(s[1])-int(s[0])):
#                    print(int(s[3])-int(s[2]),int(s[2])-int(s[1]),int(s[1])-int(s[0]))
                    print('1')
                    cnt+=1
print(cnt)'''
