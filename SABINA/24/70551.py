t = open('70551.txt').read()
t = t.replace('-', '*')
t = t.replace('*0*', '*5*')
while '**' in t:
    t = t.replace('**', '*x*')
t = t.replace('*0', 'x')
t = t.replace('x0', 'x')
a = t.split('x')
print(a)
ml = 0
for i in a:
    if len(i) > 1:
        if i[0] == '*':
            i = i[1:]
        if i[-1] == '*':
            i = i[:-1]
        ml = max(ml, len(i))
print(ml)
