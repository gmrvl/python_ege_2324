# перевод числа из десятичной системы в (какую-нибудь другую)

n = 74836  # десятичное число
n_2 = bin(n)[2:]
n_8 = oct(n)[2:]
n_16 = hex(n)[2:]

# перевод в ЛЮБУЮ систему счисления

x = 6437  # десятичное число
cc = 5  # система счисления в которую собираемся переводить
res = ''

while x != 0:
    res = str(x % cc) + res
    x //= cc

x % 5  # берет остаток от деления на 5
x / 5  # обычное деление с дробной частью
x // 5  # целочисленное деление

x = x + 1  # x += 1
x = x // 5  # x //= 5

# операторы
x = 1  # присвоение
x == 1 # проверяем равны ли х и 1
x != 1 # проверяем на неравенство
x > 1
x < 1
x >= 1
x <= 1

# перевод числа в строку и строку в число
x = 5
x_s = str(x)
x_d = int(x_s)

# строки (Строка - это набор символов)
s = '278486dsuyeiw838//83qh'
s1 = s[0] # первый символ
s_posled = s[-1] # последний символ
s_3 = s[-3] # третий с конца
s_23 = s[1:3] # срез - кусок строки с 2-го по 3-й символ

#-----------------
# max() - функция, которая ищет максимум (min() - ищет минимум)
max(1, 34, 33, 3413)

# как проверить есть ли в строке подстрока
s = '382973977792837888777'
x = '777'
if x in s:
    print('YES')
else:
    print('NO')

