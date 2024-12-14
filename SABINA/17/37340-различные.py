M = [int(x) for x in open('37340.txt')]
R = []
for i in range(0, len(M)-1):
    for j in range(i+1, len(M)):
        x, y = M[i], M[j]
        if (x - y) % 2 == 0:
            if x % 31 == 0 or y % 31 == 0:
                R.append(x + y)
print(len(R), max(R))
