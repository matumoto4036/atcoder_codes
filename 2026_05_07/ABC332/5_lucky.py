'''
5 3ND個数袋
3 5 3 6 3W重さ
'''
n,d=map(int, input().split())
w=list(map(int,input().split()))

v_min=0
bag=[0 for _ in range(n)]

def calcv():
    xb=sum(w)/d
    b=[0 for i in range(d)]
    for i in range(n):
        b[bag[i]]+=w[i]/d
    v=0
    for i in range(d):
        v+=(b[i]-xb)**2/d
    return v

for i in range(n):
    for j in range(d):
        bag[i]=j#網羅出来てない気が
        v_min=min(v_min,calcv())
print(v_min)