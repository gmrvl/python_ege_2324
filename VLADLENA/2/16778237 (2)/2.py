print ('x|y|z')

for x in range ( 0, 2 ):
    for y in range ( 0, 2 ):
        for z in range (0, 2 ):
            if ((x or y) <= (y == z)) == 0:
                print (x, y, z)