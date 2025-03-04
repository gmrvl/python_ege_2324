f = open('58532.txt').readline()
c = ''
for i in f:
    if i in 'XYZ':
        if len(c) == 0:
            c = i
        elif len(c) == 1:
            if c != i:
                c += i
        else:
            if i != c[-2] and i != c[-1]:
                c += i
            elif i != c[-1]:
                f = f.replace(c, '*', 1)
                c = c[-1] + i
            else:
                f = f.replace(c, '*', 1)
                c = i
    else:
        if len(c) > 2:
            f = f.replace(c, '*', 1)
            print(c)
        c = ''

if len(c) > 2:
    f = f.replace(c, '*', 1)
s = f.split('*')
maxi = 0
ms = ''
for i in range(0, len(s)):
    if len(s[i]) > maxi:
        maxi = len(s[i])
        ms = s[i]
print(maxi)
print(ms)

