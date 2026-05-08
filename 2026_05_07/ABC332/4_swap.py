'''
4 5             HW
1 2 3 4 5       A
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
1 3 2 5 4       B
11 13 12 15 14
6 8 7 10 9
16 18 17 20 19
'''
h,w=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(h)]
b=[list(map(int,input().split())) for _ in range(h)]

def pt(x,y):
    pt=0
    c=a
    c[x],c[x+1]=c[x+1],c[x]
    for i in range(h):
        for j in range(w):
            if a[i][j]==b[i][j]:
                pt+=1
    return pt


# def dfs(a):

#     a[i],a[j]=a[j],a[i]
#     dfs()