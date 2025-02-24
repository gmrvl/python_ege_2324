f = open('33526.txt').readline()
a = [0]*(ord('Z')+1)
print(a)
for i in range(1, len(f)-1):
    if f[i-1] == f[i+1]:
        a[ord(f[i])] += 1
print(a)
print(chr(a.index(max(a))))
print(chr(117))
