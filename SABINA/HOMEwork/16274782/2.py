# ((x → y) ∨ (y ≡ w))∧((x∨z) ≡ w)
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ((x <= y) or (y == w)) and ((x or z) == w)
                if f:
                    print(x,y,z,w)