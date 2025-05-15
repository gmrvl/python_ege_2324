'''ЕГКР 19.04.25 (Уровень: Средний)
Текстовый файл состоит из символов F, G, Q, R, S и W.
Определите в этом файле минимальное количество идущих подряд символов,
среди которых подстрока RSQ встречается ровно 130 раз, при этом искомая
 последовательность не оканчивается символом Q.
Для выполнения этого задания следует написать программу.
497'''
f = open('24_21717.txt').readline()
minn = 10000000000000
c = ''
for i in f:
    c += i
    if c.count('RSQ') < 130:
        continue
    else:
        if c[-1] == 'Q':
            continue
        else:
            if c[0:3] != 'RSQ':
                c = c[c.find('RSQ'):]
            minn = min(minn, len(c))
            c = c[3:]
print(minn)

# first = f.find('RSQ')
# f = f[first:]
# second = first + 391
# cur = f[first:second]
# while second < len(f)-1:
#     print(second)
#     if cur.count('RSQ') == 130:
#         while cur[-1] == 'Q':
#             second += 1
#             cur = f[first:second]
#         if len(cur) < min:
#             min = len(cur)
#     elif cur.count('RSQ') > 130:
#         f = f[3:]
#         first = f.find('RSQ')
#         cur = f[first:second]
#     else:
#         second += 1
#         cur = f[first:second]
# print(min)
