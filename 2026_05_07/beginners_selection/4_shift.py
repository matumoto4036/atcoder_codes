import math
n=int(input())
a=list(map(int,input().split()))
c=30
for i in range(n):
    ac=0
    tmp=int(math.log2(a[i]))
    for j in range(tmp):
        a[i]=a[i]/2
        if not a[i]==int(a[i]):
            break
        else:
            ac+=1
    c=min(c,ac)
print(c)