a = 729**7 +3**16 - 18
s = ''
while a > 0:
    s = str(a%9) + s
    a = a//9
print(s.count('0'))