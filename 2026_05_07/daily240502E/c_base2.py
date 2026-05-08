ans=0
a=list(map(int,input().split()))
for i in range(64):
    ans+=2**i*a[i]
print(ans)