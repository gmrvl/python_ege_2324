# Операнды арифметического выражения записаны в системе счисления с основанием 15:
# 123x5 + 1x233
#В записи чисел переменной x обозначена неизвестная цифра из алфавита 15-ричной системы счисления.
#Определите наименьшее значение x, при котором значение данного арифметического выражения кратно 14.
# #Для найденного значения x вычислите частное от деления значения арифметического выражения на 14 и
# #укажите его в ответе в десятичной системе счисления.
#Основание системы счисления в ответе указывать не нужно.

for x in '0123456789abcde':
    d1 = '123' + x + '5'
    d2 = '1' + x + '233'
    summ = int(d1, 15) + int(d2, 15)
    if summ % 14 == 0:
        print(summ // 14)