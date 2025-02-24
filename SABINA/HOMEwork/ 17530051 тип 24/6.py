f = open('6.txt').read()
maxx = 0
k = 0
i = 0
while i < len(f) - 2:
    if f[i] in 'CDF' and f[i + 1] in 'CDF' and f[i + 2] in 'OA':
        k += 1
        i += 3
    else:
        k = 0
    maxx = max(maxx, k)
print(maxx)

# s = open('24.txt').readline()
# s = s.replace('C', 'D').replace('F', 'D')
# s = s.replace('O', 'A')
# s = s.replace('DDA', '*')
# s = s.replace('D', ' ').replace('A', ' ')
# print(max([len(x) for x in s.split()]))