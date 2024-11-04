file = open('37340.txt')
count = 0
n, n31, c, c31 = 0, 0, 0, 0
max_n, max_n31, max_c, max_c31, max_2n31, max_2c31 = 0, 0, 0, 0, 0, 0
for digit in file:
    digit = int(digit)
    if digit % 2 == 0:
        if digit % 31 == 0:
            count += c + c31
            c31 += 1
            if digit > max_c31:
                max_c31 = digit
            elif digit > max_2c31:
                max_2c31 = digit
        else:
            count += c31
            c += 1
            if digit > max_c:
                max_c = digit
    else:
        if digit % 31 == 0:
            count += n + n31
            n31 += 1
            if digit > max_n31:
                max_n31 = digit
            elif digit > max_2n31:
                max_2n31 = digit
        else:
            count += n31
            n += 1
            if digit > max_n:
                max_n = digit
maxx = max(max_n + max_n31, max_2n31 + max_n31, max_c + max_c31, max_2c31 + max_c31)
print(count, maxx)
