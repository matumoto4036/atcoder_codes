def salesman(M,fp,a):
    sum=0
    if a>M:
        return -1
    for i in range(M):
        if a[i]==fp:
            if b[i]!=N:
                tmp=salesman(M,b[i],a+1)
                if tmp!=-1:
                    sum+=tmp
                    return sum
                else:#失敗
                    return -1
            else:#ゴール
                return sum
    return 0

N,M,K=map(int,input().split())
a=[]
b=[]
l=[]
c=[]
for i in range(M):
    num=[]
    num=list(map(int,input().split()))
    a.append(num[0])
    b.append(num[1])
    l.append(num[2])
    c.append(num[3])

while True:
    for i in range(M):
        if a[i]==1:
            for