print('x,y,z,w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (not((x or y)<=(z and w))) and (x <= w)
                if f:
                    print(x,y,z,w)