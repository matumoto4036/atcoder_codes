# n=int(input())
# ab=[list(map(int,input().split())) for _ in range(n)]
# a,b=map(list,zip(*ab))

# p=[[] for _ in range(max(a))]


# maxl=0
# for i in range(n):
#     p[a[i]-1].append(b[i])

# def search(m):
#     tmp=0
#     tmpa=len(p[m])
#     if not len(p[m])==0:
#         for i in p[m]:
#             tmp=max(search(i-1),tmp)
#     return max(tmp,m)
# print(search(0))


# from collections import defaultdict, deque
# n = int(input())
# graph = defaultdict(list)
# for _ in range(n) :
# 	a, b = map(int, input().split())
# 	graph[a].append(b)
# 	graph[b].append(a)
# que = deque()
# que.append(1)
# S = {1}
# while que:
# 	v = que.popleft()
# 	for i in graph[v]:
# 		if not i in S:
# 			que.append(i)
# 			S.add(i)
# print(max(S))


n = int(input())
graph = [[] for _ in range(100)]
for _ in range(n) :
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)

que = []
que.append(1)
S = {1}
while que:
	v = que.pop(0)
	for i in graph[v]:
		if not i in S:
			que.append(i)
			S.add(i)
print(max(S))