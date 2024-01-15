n, m = map(int, input().split())
if n == 0 or m == 0:
    print(0)
    exit(0)
a = []
b = [[0]*n, [0]*n]
for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)
    b[0][i] = max(row)
    b[1][i] = sum(row)

max_b = max(b[0])

c = b[0].count(max_b)
if c == 1:
    print(b[0].index(max_b))
else:
    p = 0
    max_s = 0
    for i in range(n):
        if b[0][i] == max_b and b[1][i] > max_s:
            p = i
            max_s = b[1][i]
    print(p)

    # sum = 0
    # res = 0
    # n, m = map(int, input().split())
    # for i in range(n):
    #     s = 0
    #     mx = 0
    #     a = map(int, input().split())
    #     a = list(a)
    #     for j in a:
    #         s += j
    #         if mx < j:
    #             mx = j
    #     if mx > res:
    #         res, ii, sum = mx, i, s
    #     elif res == mx and s > sum:
    #         res, ii, sum = mx, i, s
    # print(ii)ii
