# 8x71 13 + 3xDF 17
for x in range(0,13):
    x1 = int(x)
    a1 = 8*13**3 + x1*13**2 + 7*13**1 + 1
    a2 = 3*17**3 + x1*17**2 + 13*17**1 + 15
    summ = a1 + a2
    if summ % 197 == 0:
        print(summ // 197)

