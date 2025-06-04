f = open('12.csv')
for i in f:
    s = list(map(int,i.split(';')))
