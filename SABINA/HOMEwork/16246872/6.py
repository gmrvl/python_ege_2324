for a in range(1, 70):
    for b in range(1, 70):
        for c in range(1, 70):
            s = '0' + '1'*a + '2'*b + '3'*c + '0'
            while not '00' in s:
                s = s.replace('01', '210', 1)
                s = s.replace('02', '3101', 1)
                s = s.replace('03', '2012', 1)
            odin = s.count('1')
            dva = s.count('2')
            tri = s.count('3')
            if odin == 70 and dva == 56 and tri == 23:
                print(a)
                print(b)
                print(c)

