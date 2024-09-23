a = [1,2,2,3,4,5]
s = set(a)
sr1 = 0
count = 0
if len(s) == 5:   #то есть повторяющихся чисел всего два
    for k in range(0, len(a)):
        if a.count(a[k]) == 2:
            sr1 = (2 * int(a[k]))/2
            cnt = 0
            if a.count(a[k]) == 1:
                cnt = 0 + int(a[k])
            print(cnt)
            sr2 = cnt/4
            if sr1 < sr2:
                count +=1
print(count)