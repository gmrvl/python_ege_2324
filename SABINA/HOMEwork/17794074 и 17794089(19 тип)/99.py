count = 0
f = 0
for s in open('9_58322.csv'):
    M = sorted([int(x) for x in s.split(';')])
    if M[-1] ** 2 > (M[0] * M[1] * M[2]):
        count += 1
    if all(M[1] - M[0] == M[i+1] - M[i] for i in range(len(M)-1)):
        f += 1
print(count, f)