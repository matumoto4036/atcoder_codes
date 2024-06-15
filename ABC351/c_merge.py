n=int(input())
a=list(map(int,input().split()))
q=[]
for i in range(n):
    q.append(a[i])
    while len(q)>1:
        if q[len(q)-1]==q[len(q)-2]:
            tmp=q[len(q)-1]
            q.pop(len(q)-1)
            q.pop(len(q)-1)
            q.append(tmp+1)
        else:break
print(len(q))