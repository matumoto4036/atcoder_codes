n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
minarg=10e9
for i in range(n):
    for j in range(m):
        minarg=min(minarg,abs(a[i]-b[j]))
print(minarg)