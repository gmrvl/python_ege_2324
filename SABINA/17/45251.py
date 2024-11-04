file = open('45251.txt')
min21 = 100000
for digit in file:
    digit = int(digit)
    if digit % 21 == 0 and digit < min21:
        min21 = digit

file = open('45251.txt')
count = 0
maxx = 0
f = file.readline()
for s in file:
    f, s = int(f), int(s)
    if f % min21 == 0 or s % min21 == 0:
        count += 1
        if f + s > maxx:
            maxx = f + s
    f = s
print(count, maxx)
