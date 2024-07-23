#Игорь составляет пятизначные числа, используя цифры девятеричной системы счисления.
#Сколько различных чисел может составить Игорь, в которых ровно две цифры 3 и нечётные цифры не стоят рядом с цифрой 2?
count = 0
for i in range(9**4, 9**5):
    a = ''
    d = '012345678'
    f = True
    while i > 0:
        a = str(i % 9) + a
        i //= 9
    if a.count('3') == 2:
        if '2' in a:
            if a[0] == '2' and int(a[1]) % 2 == 1:
                f = False
            elif a[4] == '2' and int(a[3]) % 2 == 1:
                f = False
            elif a[1] == '2' and (int(a[0]) % 2 == 1 or int(a[2]) % 2 == 1):
                f = False
            elif a[2] == '2' and (int(a[1]) % 2 == 1 or int(a[3]) % 2 == 1):
                f = False
            elif a[3] == '2' and (int(a[2]) % 2 == 1 or int(a[4]) % 2 == 1):
                f = False
    else:
        f = False
    if f:
        count += 1
print(count)
