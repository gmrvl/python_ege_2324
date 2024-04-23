a = 9**8 + 3**5 - 9
a_t = ''
while a > 0:
    a_t = str(a % 3) + a_t
    a //= 3
print(a_t.count('2'))
