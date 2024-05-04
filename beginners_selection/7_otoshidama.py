n,y=map(int,input().split())
for i in range(n+1):
    if i*10000>y:break
    for j in range(n-i+1):
        tmp=i*10000+j*5000
        if tmp>y:break
        if (y-tmp)/1000==n-i-j:
            print(i,j,n-i-j)
            exit()
print(-1,-1,-1)