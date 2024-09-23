count = 0
f = open('09 (1)csv.csv')
for i in f:
    a = list(map(int,i.split(';')))
    a = sorted(a)
    s = set(a)
    if len(a) == len(s) :
