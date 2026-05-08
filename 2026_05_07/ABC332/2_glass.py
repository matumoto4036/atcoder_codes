'''
5 300 500KGM繰り返し グラス まぐ
'''
k,G,M=map(int,input().split())
def utusu(g,m):
    if g==G:
        g=0
    elif m==0:
        m=M
    else:
        tmp=min(m,G-g)
        g+=tmp
        m-=tmp
    return g,m

g,m=0,0
for i in range(k):
    g,m=utusu(g,m)
print(g,m)