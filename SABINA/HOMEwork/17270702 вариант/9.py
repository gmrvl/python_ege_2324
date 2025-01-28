f = open('09 (9).csv')
cnt = 0
for i in f:
    r = []
    summ = 0
    s = list(map(int,i.split(';')))
    if (len(set(s)) != len(s)) and s.count(max(s)) == 1:
        for k in range(0, len(s)):
            if s.count(s[k]) > 1:
                r.append(int(s[k]))
                summ += s[k]
        if summ < max(s):
            cnt+=1
print(cnt)

# f = open('09 (9).csv')
# cnt = 0
# for s in f:
#     a = list(map(int, s.split(';')))
#     if len(set(a)) != len(a):
#         if a.count(max(a)) == 1:
#             suma = 0
#             for i in range (0,len(a)):
#                 if a.count(a[i]) > 1:
#                     suma += a[i]
#             if suma < max(a):
#                 cnt += 1
# print(cnt)