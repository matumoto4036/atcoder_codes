'''
3 3
2 1 2
2 2 3
2 1 3
NM 人数 舞踏会回数
k x_k
k_m x_k_m
'''
n,m=map(int,input().split())
ka=[]
x=[]
for i in range(m):
    tmp=list(map(int,input().split()))
    ka.append(tmp[0])
    x.append(tmp[1:])


check=[[False for _ in range(n)] for _ in range(n)]
for i in range(n-1):
    for j in range(i,n):
        for k in range(m):
            if i+1 in x[k] and j+1 in x[k]:
                check[i][j]=True

        if not check[i][j]:
            print("No")
            exit()
print("Yes")

