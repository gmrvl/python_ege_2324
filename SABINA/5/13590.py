# Автомат получает на вход трёхзначное число. По этому числу строится новое число по следующим правилам.
# 1.Перемножаются отдельно первая и вторая цифры, а также вторая и третья цифры.
# 2.Полученные два числа записываются друг за другом в порядке невозрастания (убывание) без разделителей.
# Пример. Исходное число: 179. Произведения: 1*7 = 7; 7*9 = 63. Результат: 637.
# Укажите наименьшее число, при обработке которого автомат выдаёт результат 205.
for i in range(100, 1000):
    s = str(i)
    a1 = s[0]
    a2 = s[1]
    a3 = s[2]
    pr1 = int(a1) * int(a2)
    pr2 = int(a2) * int(a3)
    if pr1 < pr2:
        n = str(pr2) + str(pr1)
    else:
        n = str(pr1) + str(pr2)
    if n == '205':
        print(i)
        break