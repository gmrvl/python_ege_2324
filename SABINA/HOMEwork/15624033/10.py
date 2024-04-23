count = 0
s = '1' * 40 + '2' * 10 + '3' * 8
while '01' in s or '02' in s or '03' in s:
    s = s.replace('01','2302', '1')
    s = s.replace('02', '10', '1')
    s = s.replace('03', '201', '1')
    count += 1
    print(count)

# for k1 in range(50):
#     for k2 in range(50):
#         for k3 in range(50):
#             s='0'+k1*'1'+k2*'2'+k3*'3'
#             while '01' in s or '02' in s or '03' in s:
#                 s=s.replace('01','2302',1)
#                 s=s.replace('02','10',1)
#                 s=s.replace('03','201',1)
#             if s.count('1')==40 and s.count('2')==10 and s.count('3')==8:
#                 print (k1)

