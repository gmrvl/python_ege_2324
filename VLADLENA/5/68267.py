for i in range(100, 10000):
    s = str(i)
    troiki = []
    for j in range(len(s) - 2):
        troiki.append(s[j:j+3])
    troiki = [int(x) for x in troiki]
    res = max(troiki) - min(troiki)
    if res == 623:
        print(i)
        break
