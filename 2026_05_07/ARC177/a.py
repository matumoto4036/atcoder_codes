a=list(map(int,input().split()))
c=[1,5,10,50,100,500]
n=int(input())
x=list(map(int,input().split()))
for i in range(n):
    for j in reversed(range(6)):
        if x[i]>=c[j]:
            tmp=a[j]
            a[j]=max(0,a[j]-x[i]//c[j])
            x[i]=x[i]-min(tmp,x[i]//c[j])*c[j]
    
if sum(x)==0:print("Yes")
else:print("No")
        