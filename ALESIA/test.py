s = '0101010'

s = s.replace('0', '*')
s = s.replace('1', '0')
s = s.replace('*', '1')

print(s)
