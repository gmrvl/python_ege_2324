f = open('4.txt').read()
f = f.replace('-', '*')
f = f.replace('*0*', '*9*')
while '**' in f:
    f = f.replace('**','*x*')
f = f.replace('*0','x')
f = f.replace('x0', 'x')
a = f.split('x')
maxx = 0
print(a)
for i in a:
    if len(i) > 1:
        if a[0] == '*' and a[1] == 'B':
            i = i[1:]
            maxx = max(maxx, len(i))
        if a[-1] == '*' and a[0] == 'B':
            i = i[:-1]
            maxx = max(maxx, len(i))
print(a)
print(maxx)
