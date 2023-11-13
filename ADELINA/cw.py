x = int(input())
d = int(input())
n = int(input())

res = [x]
for i in range(1, n):
    res.append(res[i - 1] + d)
for i in res:
    print(i, end=' ')