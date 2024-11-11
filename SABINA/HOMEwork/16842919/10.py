file = open('10.txt')
cnt = 0
maxx = -20000
first = file.readline()
for second in file:
    first, second = int(first), int(second)
    if first % 160 != second % 160:
        if first % 7 == 0 or second % 7 == 0:
            cnt += 1
            if first + second > maxx:
                maxx = first + second
    first = second
print(cnt, maxx)