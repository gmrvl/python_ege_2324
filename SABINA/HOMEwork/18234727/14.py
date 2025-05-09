for p in range(1,37):
    for x in range(1,p):
        for y in range(1,p):
            s1 = x*p**3 + x*p**2 + x*p**1 + 8*p**0
            s2 = 4*p**3 + 3*p**2 + x*p**1 + 9
            s3 = y*p**3 + y*p**2 + 0*p**1 + 4
            if s1 + s2 == s3:
                print(y*p**2 + y*p**1 + x)



'''for x in '0123456789abcdefghijklmnopqrstuvwxyz':
#    print(x)
    for y in '0123456789abcdefghijklmnopqrstuvwxyz':
        for p in range(1,37):
            s1 = int(str(x)+str(x)+str(x)+'8')
            s2 = int('43'+str(x)+'9')
            r = int(str(y)+str(y)+'04')
            s1 = s11
            s2 = s22
            r = r2
            
            if s11+s22 == r2:'''

