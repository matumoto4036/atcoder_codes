from collections import defaultdict, deque
n,m=map(int,input().split())
graph=defaultdict(list)
min=10e9*n
c=[[]]

for i in range(m):
    k,c=map(int,input().split())
    a=list(map(int,input().split()))
    for j in range(k):
        for l in range(k):
            if j==l or a[l] in graph[a[j]]:continue
            graph[a[j]].append(a[l])

que = deque()
que.append(1)
S = {1}
while que:
	v = que.popleft()
	for i in graph[v]:
		if not i in S:
			que.append(i)
			S.add(i)
                  
if len(S)==n:
    print(0)
else:
    print(-1)