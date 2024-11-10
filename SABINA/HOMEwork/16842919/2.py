f = open('2.txt')
cnt = 0
maxx = -1
first = f.readline()
for second in f:
    first, second = int(first), int(second)
    if (first - second) % 36 == 0 and \
        first % 13 == 0 or second % 13 == 0:
        cnt+=0
        if first - second > maxx:
            maxx = first - second
    first = second
print(cnt,maxx)