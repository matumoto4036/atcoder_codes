n=int(input())
sum=0
d=[]
for i in range(n):
    sc=input().split()
    d.append(sc[0])
    sum+=int(sc[1])
sum=sum%n
d.sort()
print(d[sum])
