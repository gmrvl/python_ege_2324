correct = []
our = []

count = 0
m = 10000000
f = open('12.txt')
l = [int(i) for i in f]
max_dvy = 0
for i in range(len(l)):
    if abs(l[i]) % 100 == 13:
        max_dvy = max(max_dvy, l[i])
for i in range(len(l) - 2):
    c = 0
    s = [l[i], l[i+1],  l[i+2]]
    for x in s:
        if 99 < abs(x) < 1000:
            c += 1
    if c == 2 and sum(s) < max_dvy:
        m = min(m, (l[i] + l[i+1] + l[i+2]))
        count += 1
        correct.append(s)
print(max_dvy)

cnt = 0
minn = 100000
maxx = -1
r = [int(i) for i in open('12.txt')]
for i in r:
    if i % 100 == 13:
        if i > maxx:  # maxx = max(i, maxx)
            maxx = i
f = open('12.txt')
fst = f.readline()
sec = f.readline()
for thd in f:
    a = [len(fst) - 1, len(sec) - 1, len(thd) - 1]
    if (a.count(3) == 2) and ((int(fst) + int(sec) + int(thd)) < maxx):
        cnt += 1
        our.append([int(fst), int(sec), int(thd)])
        if int(fst) + int(sec) + int(thd) < minn:
            minn = int(fst) + int(sec) + int(thd)
    fst = sec
    sec = thd
print(maxx)
# print(cnt, minn)

# print(count, m)
for i in range(len(correct)):
    if correct[i] != our[i]:
        print(i, correct[i], correct[i+1], our[i])
        break