n = int(input())
a = []
for i in range(n * 2 + 1):
    a.append([0] * (n * 2 + 1))

array_size = n * 2 + 1

i = array_size // 2
j = i

cur_num = 0
limit = 2
step = 1
turn = 0  # 0 - up 1 left 2 down 3 right
while i != -1:
    a[i][j] = cur_num
    cur_num += 1

    if step == 0:
        limit += 1
        step = limit // 2
        turn = (turn + 1) % 4

    step -= 1
    if turn == 0:
        i -= 1
    elif turn == 1:
        j -= 1
    elif turn == 2:
        i += 1
    else:
        j += 1

for i in range(n * 2 + 1):
    print(*a[i])
