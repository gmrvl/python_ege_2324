n, m = map(int, input().split())
x, y = map(int, input().split())

ans = [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]

for res in ans:
    i = res[0]
    j = res[1]
    if 0 <= i < n and 0 <= j < m:
        print(i, j)
