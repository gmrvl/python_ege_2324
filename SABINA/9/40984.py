count = 0
f = open("09 (1).csv")
for i in f:
    a = list(map(int, i.split(','))) #sorted - сортировка по возрастанию; split разделение на ячейки по знаку ';'
    # for j in a:
    #     j = int(j)
    a = sorted(a, reverse=True) # реверс - это наоборот(сортировка по убыванию)
    if a[0]*a[1] < a[1]*a[2] + a[0]*a[2]:
        count += 1
print(count)

