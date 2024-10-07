a = 4**34 + 5*(4**22) + 4**13 + 2*(4**9) + 82
r = ''
ahex = hex(a)[2:]
#while a > 0:
 #   r = str(a % 16) + r
  #  a = a // 16
print(len(set(ahex)))
