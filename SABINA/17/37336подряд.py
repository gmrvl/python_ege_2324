file = open('37336.txt')
count = 0
maxx = -20000
first = file.readline()
for second in file:
    first, second = int(first), int(second)
    if first % 3 == 0 or second % 3 == 0:
        count += 1
        if first + second > maxx:
            maxx = first + second
            # maxx = max(maxx, fst + sec)
    first = second
print(count, maxx)