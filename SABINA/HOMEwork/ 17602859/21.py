def w1(s):
    return (s+1) >= 64 or (s*3) >= 64
def l1(s):
    return (not(w1(s))) and w1(s+1) and w1(s*3)
def w2(s):
    return l1(s+1) or l1(s*3)
def l2(s):
    return w1(s+1) and w2(s*2) or w2(s+1) and w1(s*2)

for s in range(1,64):
    if l2(s):
        print(s)
