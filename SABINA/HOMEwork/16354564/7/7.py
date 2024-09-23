f = open('7.csv')
count = 0
for i in f:
    a = list(map(int,i.split(';')))
    s = set(a)
    sr1 = 0
    if len(s) == 5:   #то есть повторяющихся чисел всего два
        copy = sum(a) - sum(s)
        if (2*copy)/2 < (sum(s) - copy)/4:
            count += 1
print(count)