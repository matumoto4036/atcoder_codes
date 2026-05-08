n=int(input())
asum=0
bmax=0
for i in range(n):
    a,b=map(int,input().split())
    bmax=max(b-a,bmax)
    asum+=a
print(asum+bmax)