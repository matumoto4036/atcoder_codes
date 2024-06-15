import math
h=int(input())
ht=0
c=0
while h>=ht:
    ht+=2**c
    c+=1
print(c)