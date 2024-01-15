n = 2 * int(input()) + 1
w = 0
b = [[w]]

for i in range(2 * (n - 1)):
    b = list(map(list, zip(*b)))
    b.reverse()
    for h in range(len(b)):
        w += 1
        b[h].append(w)

b = list(map(list, zip(*b)))
b.reverse()
for i in b:
    print(*i)
print()