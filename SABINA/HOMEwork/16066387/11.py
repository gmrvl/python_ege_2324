for x in range(0, 1000):
    for y in range(0, 1000):
        for z in range(0, 1000):
            a = '0' + '1'*z + '3'*x + '2'*y + '0'
while not '00' in a:
    b = a.replace('033','1302', 1)
    b = a.replace('03','120',1)
    b = a.replace('023','203',1)
    b = a.replace('02','20',1)
if b.count('1') == 333 and b.count('2') == 819 and b.count('3') == 181:
    print(y)
