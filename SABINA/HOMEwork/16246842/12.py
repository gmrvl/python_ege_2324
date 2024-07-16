#Сколько существует чисел, восьмеричная запись
#которых содержит 5 цифр, причем в записи нет цифры 1.
#Также все цифры записи различны и никакие две чётные
#и две нечётные цифры не стоят рядом.
# 0 2 3 4 5 6 7
count = 0
for i in range(8**4, 8**5):
    a = ''
    d = '0234567'
    f = True
    while i > 0:
        a = str(i % 8) + a
        i = i // 8
    a = int(a)
    s = str(a)
    if not '1' in s:
        for a in d:
            if s.count(a) > 1:
                f = False
        if f and (int(s[0]) % 2 + int(s[1]) % 2 == 1) and (int(s[1]) % 2 + int(s[2]) % 2 == 1) and (int(s[2]) % 2 + int(s[3]) % 2 == 1) and (int(s[3]) % 2 + int(s[4]) % 2 == 1):
            count = count + 1
print(count)

