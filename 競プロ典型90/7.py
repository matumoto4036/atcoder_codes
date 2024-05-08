from bisect import bisect_left
INF = 2 ** 60
n=int(input())
a=list(map(int,input().split()))
a.sort()
q=int(input())
ans=[]
for i in range(q):
    b=int(input())
    j=bisect_left(a,b)
    res=INF
    if j<n:#0-j-n-1
        res=min(res,abs(b-a[j]))
    if j>0:#1-j-n
        res = min(res, abs(b - a[j-1]))
    ans.append(res)
    # tmp=[]
    # for i in range(n):
    #     tmp.append(abs(a[i]-b))
    # ans.append(min(tmp))
print(*ans,sep="\n")