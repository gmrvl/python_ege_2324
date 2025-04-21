
f = open('zadanie24_1.txt').read()
d = ''
maxx = 0
for i in f:
    if i == 'B':
        d += i
    else:
        maxx = max(maxx, len(d))
        d = ''
maxx = max(maxx, len(d))
print(maxx)

# f = open('zadanie24_1.txt').readline()
# f = f.replace('A',' ')
# f = f.replace('C',' ')
# f = f.split()
# print(max(len(x) for x in f))
