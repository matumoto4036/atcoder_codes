h,w=map(int,input().split())
s=[input() for _i in range(h)]
def check(a,b):
    if h-1>=a>=0 and w-1>=b>=0:
        return True
    return False

def checkhash(a,b):
    if a+1>1:
        if s[a-1,b]=="#":
            return False
    if w>a+1:
        if s[a+1,b]=="#":
            return False
    if b+1>1:
        if s[a,b-1]=="#":
            return False
    if h>b+1:
        if s[a,b+1]=="#":
            return False
    return True

idou=[[-1,0],[1,0],[0,-1],[0,1]]
c=0
path=[]
q=[]
for i in range(h):
    for j in range(w):
        if s[i][j]=="#":continue
        path.append([i,j])
        while True:
            for k in idou:
                ni,nj=i+k[0],j+k[1]
                if check(ni,nj):
                    path.append([ni,nj])
                    if s[ni,nj]=="#": break
                    