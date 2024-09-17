count = 0
for i in range(12**4,12**5):
    a = ''
    while i > 0:
        ost = i % 12
        if ost > 8:
            a = '*' + a
        else:
            a = str(ost) + a
        i = i // 12
    if a.count('7') == 1 and a.count('*') <= 3:
        count += 1
print(count)

