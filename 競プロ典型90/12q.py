# h,w=map(int,input().split())
# q=int(input())
# masu=[[0]*w for _ in range(h)]

# def dfs(a,b,c,d,path):
#     if (c,d) in path:return True
#     idou=[(-1,0),(1,0),(0,-1),(0,1)]
#     for i in idou:
#         if 0<=a+i[0]<w and 0<=b+i[1]<h:
#             if a+i[0]==c and b+i[1]==d:
#                 path.append([c,d])
#                 return True
#             if masu[a+i[0]][b+i[1]]==1:
#                 path.append([a+i[0],b+i[1]])
#                 if dfs(a+i[0],b+i[1],c,d,path):return True
#     return False

# for i in range(q):
#     tmp=list(map(int,input().split()))
#     if tmp[0]==1:
#         masu[tmp[1]-1][tmp[2]-1]=1
#     elif tmp[0]==2:
#         if masu[tmp[1]-1][tmp[2]-1]==1 and masu[tmp[3]-1][tmp[4]-1]==1 :
#             if dfs(tmp[1]-1,tmp[2]-1,tmp[3]-1,tmp[4]-1,[(tmp[1]-1,tmp[2]-1)]):
#                 print("Yes")
#             else:
#                 print("No")
#         else:
#             print("No")

from atcoder.dsu import DSU

def f(x, y):
  return (W + 1) * x + y

H, W = map(int, input().split())
Q = int(input())

uf = DSU((H + 1) * (W + 1))
r = set()

for i in range(Q):
  q = list(map(int, input().split()))
  if q[0] == 1:
    s, t = q[1:]
    r.add(f(s, t))
    for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
      if f(s + x, t + y) in r:
        uf.merge(f(s, t), f(s + x, t + y))
  else:
    s, t, x, y = q[1:]
    if f(s, t) in r and f(x, y) in r and uf.same(f(s, t), f(x, y)):
      print("Yes")
    else:
      print("No")
