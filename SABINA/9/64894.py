f = open('09.csv')
k = 0
arow = [[int(x) for x in s.split(',')] for s in f]
acol = [[arow[i][j] for i in range(len(arow))] for j in range(6)]
for i in range(len(arow)):
    kint = 0
    for j in range(6):
        x = arow[i][j]
        if arow[i].count(x) == 1 and acol[j].count(x) > 150:
            kint += 1
    if kint >= 5:
        k += 1
print(k)

# f = open('09.csv')
# k = 0
# arow = [[int(x) for x in s.split(',')] for s in f]
# for i in range(len(arow)):
#     kint = 0
#     for j in range(6):
#         x = arow[i][j]
#         if arow[i].count(x) == 1:
#             kcol = 0
#             for k in range(len(arow)):
#                 if arow[k][j] == x:
#                     kcol += 1
#             if kcol > 150:
#                 kint += 1
#     if kint >= 5:
#         k += 1
# print(k)