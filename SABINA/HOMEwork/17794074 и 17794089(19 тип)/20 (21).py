def win1(s):
    return (s+1) >= 31 or (s*3 - 2)>= 31
def los1(s):
    return not(win1(s)) and win1(s+1) and win1(s*3 - 2)
def win2(s):
    return los1(s+1) or los1(s*3 - 2)
for s in range(1,31):
    if win2(s):
        print(s)
