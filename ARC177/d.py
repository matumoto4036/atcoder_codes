n,h=map(int,input().split())
x=list(map(int,input().split()))
nx=[]
for i in range(n):
    nx.append([i,x[i]])

nx=sorted(nx,key=lambda x: x[1])

pro=[0]*n
life=[1]*h
def dfs(l0,t):
    
    l1=l0
    l0[t]=0
    l1[t]=0
    pra=[y[0] for y in nx].index(t)
    for i in reversed(range(0,pra)):
        if l0[i]==0:break
        if nx[i]-nx[i-1]<h:break
        l0[i]=0
    if sum(l0)==0:pro[t]+=1/2**(t+1)
    else:dfs(l0,t+1)

    for i in range(pra+1,n):
        if l1[i]==0:break
        if nx[i+1]-nx[i]<h:break
        l1[i]=0
    if sum(l1)==0:pro[t]+=1/2**(t+1)
    else:dfs(l1,t+1)
    return

dfs(life,0)
for i in range(n):
    pro[i]=pro[i]*2**i
print(pro)