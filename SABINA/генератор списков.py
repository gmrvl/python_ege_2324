#генерируется список из иксов
# идет перебор иксов

a = [x for x in range(10)]
print(a)

# список с условием
b = [x for x in range(10) if x % 2 == 0]
print(b)

# использование данных
file = '1 2 3 4 5'
c = [int(x) for x in file.split()]
print(c)