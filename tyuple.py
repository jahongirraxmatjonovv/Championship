from collections import namedtuple

olma = namedtuple('olma',"x y z")
pt1 = olma(1,2,3)

print(pt1)    
print(pt1.x) 
   
for i in pt1:
    print(i)
    
k = set(pt1)
print(k)    