a = []
for i in range(9):
    a.append(list(map(int, input().split())))
ok = True
for i in range(9):
    stroki = [0]*9
    stolby = [0]*9
    for j in range(9):
        stroki[a[i][j] - 1] += 1
        stolby[a[j][i] - 1] += 1
    for r in range(9):
        if stolby[r] != 1 or stroki[r] != 1:
            ok = False
            break
    if not ok:
        break
for x in range(0, 9, 3):
    for y in range(0, 9, 3):
        blok = [0]*9
        blok[a[x][y] - 1] += 1
        blok[a[x+1][y] - 1] += 1
        blok[a[x+2][y] - 1] += 1
        blok[a[x][y+1] - 1] += 1
        blok[a[x][y+2] - 1] += 1
        blok[a[x+1][y+1] - 1] += 1
        blok[a[x+2][y+2] - 1] += 1
        blok[a[x+1][y+2] - 1] += 1
        blok[a[x+2][y+1] - 1] += 1
    for r in range(9):
        if blok[r] != 1:
            ok = False
            break
    if not ok:
        break

if ok:
    print('yes')
else:
    print('no')
