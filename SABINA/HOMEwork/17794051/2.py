print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f1 = (w == x) and (y <= z)
                f2 = (w <=x) <= (y == z)
                if f2:
                    print(x,y,z,w)