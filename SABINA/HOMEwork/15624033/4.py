print('x,y,z,w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f= (w<=y) and ((not(y))==x)and(z or z)
                if f:
                    print(x,y,z,w)

