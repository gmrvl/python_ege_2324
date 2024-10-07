s = 13*'1' + 18*'2'
r = ''
a = ''
for a in range(100000):
    a = str(a)
    a = '0' + a

   # print(a)
    if a[0] == a[-1] == 0 and '0' < 3:
        while '00' not in a:
            a = a.replace('01', '220',1)
            a = a.replace( '02', '1013', 1)
            a = a.replace( '03', '120', 1 )
        a = r
        if r == s:
            print(s)

