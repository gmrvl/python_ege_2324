#Определите количество четырехзначных чисел, записанных в десятичной системе счисления,
# в записи которых все цифры различны и никакие две чётные и две нечётные цифры не стоят рядом.
count = 0
for i in range(1000, 10000):
    s = str(i)
    r = str(set(s))

    if len(s) != len(r) and int(s[0]) % 2 == 1 and int(s[1]) % 2 == 0 and int(s[2]) % 2 == 1 and int(s[3]) % 2 == 0 :
        count += 1
    else:
        count += 0
    if len(s) != len(r) and int(s[0]) % 2 == 0 and int(s[1]) % 2 == 1 and int(s[2]) % 2 == 0 and int(s[3]) % 2 == 1:
        count += 1
    else:
        count += 0
print(count)



