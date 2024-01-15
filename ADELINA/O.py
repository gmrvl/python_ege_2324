n, m, k = map(int, input().split())
a, mines = [], []
for i in range(n):
    a.append([0] * m)

for i in range(k):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    mines.append([x, y])
    a[x][y] = '*'

for mine in mines:
    i = mine[0]
    j = mine[1]
    position = [[i - 1, j], [i + 1, j], [i, j - 1],
                [i, j + 1], [i - 1, j - 1], [i - 1, j + 1],
                [i + 1, j - 1], [i + 1, j + 1]]
    for point in position:
        x, y = point[0], point[1]
        if 0 <= x < n and 0 <= y < m and a[x][y] != '*':
            a[x][y] += 1

for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            print('.', end='')
        else:
            print(a[i][j], end='')
    print()


