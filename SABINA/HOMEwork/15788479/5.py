print('x,y,z,w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (((not(z)) or w) and ((not(x)) == y)) <= (x and z)
                if not f:
                    print(x,y,z,w)