f = open('1.txt')
cnt = 0
maxx = -1
first = f.readline()
for second in f:
    first, second = int(first), int(second)
    if (first + second) % 2 == 1 and (first * second) % 5 == 0:
        cnt+=1
        if (first + second) > maxx:
            maxx = first + second
    first = second
print(cnt, maxx)