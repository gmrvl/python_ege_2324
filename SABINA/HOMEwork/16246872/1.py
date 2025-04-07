s = '2'+'9'*100
while '19 и смешанный' in s or '299' in s or '3999' in s:
    s = s.replace('19 и смешанный' , '2', 1)
    s = s.replace('299', '3', 1)
    s = s.replace('3999', '1', 1)
print(s)
