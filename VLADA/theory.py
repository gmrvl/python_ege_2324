# перевести число в 2/8/16

a = bin(5)[2:] # двоичная
a = oct(5)[2:] # восьмиричная
a = hex(5)[2:] # шеснадцатиричная

# как вывести на экран

print(a)

# строки - строка это набор символов, заключенный в кавычки

b = 'hello, world'
c = b[1:5]  # у строки b возьми с 1 по 4 символ
k = b[4:]  # с 4 по последний
m = b[:5]  # c начала по 4
print(c)

print(a[2:])