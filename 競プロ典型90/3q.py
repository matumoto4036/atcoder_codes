# n=int(input())
# from collections import defaultdict, deque
# c=defaultdict(list)
# for i in range(n-1):
#     a,b=map(int,input().split())
#     c[a].append(b)
#     c[b].append(a)

# mx=0
# que=deque()
# path=[]

# for i in range(n):
#     que=deque()
#     path=[]
#     que.append(i+1)
#     path.append(i+1)
#     while que:
#         tmp=que.popleft()
#         for j in c[tmp]:
#             if not j in path:
#                 path.append(j)
#                 que.append(j)
#     mx=max(mx,count)
# print(mx)



# I=input
# R=range
# P=print
# def IP():return int(I())
# def IPS():return I().split()
# def MPS():return map(int,I().split())
# def LPS():return list(map(int,I().split()))

# from networkx import*
# n=IP()
# g=Graph([[*MPS()]for _ in R(n-1)])
# v=[*bfs_edges(g,1)][-1][1]
# P(eccentricity(g,v)+1)




# N=int(input())
# michi = [set() for _ in range(N)]

# for _ in range(N-1):
#   A,B=map(int,input().split())
#   A-=1
#   B-=1
#   michi[A].add(B)
#   michi[B].add(A)
  
# def dfs(num, seen): #スタートと道の通ったか否か
#   #最長距離と最も離れた頂点を返す
#   l = 0
#   saicho = num

#   seen[num]=True
#   for a in michi[num]:
#     if not seen[a]:
#       d = dfs(a, seen)
#       if l < d[0]+1:
#         l = d[0]+1
#         saicho = d[1]
  
#   return (l,saicho)
  
# print(dfs(dfs(0, [False] * N)[1], [False] * N)[0]+1)

# 入力
N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1  # 0-indexed に
    G[a].append(b)
    G[b].append(a)

# 頂点 s から DFS (ここではスタックを使う)
def dfs(s):
    # 頂点 s からの距離
    dist = [-1] * N
    dist[s] = 0
    # スタックで DFS
    st = [s]
    while st:
        v = st.pop()#右から
        for nv in G[v]:
            if dist[nv] == -1:
                st.append(nv)
                dist[nv] = dist[v] + 1
    # リターン
    return dist

# 頂点 0 から
dist0 = dfs(0)
mv = max(enumerate(dist0), key=lambda x: x[1])[0]
distmv = dfs(mv)
print(max(distmv) + 1)