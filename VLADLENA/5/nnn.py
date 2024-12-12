count = 0
for x1 in '13579':
    for x2 in '13579':
        for x3 in '13579':
            for x4 in '13579':
                m = [int(x1)+int(x2), int(x3)+int(x4)]
                if min(m) == 6 and max(m) == 16:
                    count += 1
print(count)

#######
sum1 = x1
sum2 = x2
sum3 = x3
maxx = max(sum1, sum2, sum3)
aver = sum(sum1, sum2, sum3) - maxx - min(sum1, sum2, sum3)

