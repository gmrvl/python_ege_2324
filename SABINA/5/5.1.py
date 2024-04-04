x = 15  # десятичное число
cc = 3  # система счисления в которую собираемся переводить
res = ''
x = 90
while x != 0:
    res = str(x % cc) + res
    x //= cc

print(res, cc, x)
