# import math
# n=int(input())
# s=sorted(list(input()))
# c=0
# max=math.pow(10,n)
# for i in range(1,math.pow(max,1/2)):
#     t=str(i**2)
    

n=int(input())
s=sorted(list(input()))
a=set()
for i in range(10**7):
  t=str(i**2)
  if len(t)>n:
    break
  t=t.zfill(n)
  if sorted(list(t))==s:
    a.add(t)
print(len(a))