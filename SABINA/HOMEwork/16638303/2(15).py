for a in range(0, 1000):
     fl = True
     for x in range(0, 1000):
         f = x&29 != 0 <= ( x&17 == 0 <= x&a !=0)
         if not f:
             fl = False
             break
     if fl:
         print(a)
         break