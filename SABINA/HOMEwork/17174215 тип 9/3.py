# cnt = 0
# f = open('3.csv')
# for i in f:
#     a = list(map(int, i.split(';')))
#     a = sorted(a)
# #    print(a)
#     if int(a[0]) + int(a[1]) < int(a[3]):
#         cnt += 1
# print(cnt)

cnt = 0
f = open('3.csv')
for s in f:
    a = list(map(int,s.split(';')))
    a.sort()
    if a[0] + a[1] < a[3]:
        cnt+=1
print(cnt)