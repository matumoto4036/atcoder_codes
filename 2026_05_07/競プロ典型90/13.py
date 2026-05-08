# n,m=map(int,input().split())
# from collections import defaultdict, deque
# st=defaultdict(list)

# for i in range(m):
#     a,b,c=map(int,input().split())
#     st[a].append([b,c])
#     st[b].append([a,c])

# que=deque()
# que.append(1)
# path=[]
# while que:
#     v=que.popleft()
#     path.append
#     for i in st[v]:
#         if i[0] in path:continue
#         path.append(i[0])
        
import heapq
def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        graph[a].append((b, c))
        graph[b].append((a, c))
    # 頂点 k からダイクストラ法で各頂点までの最短路長を求める
    def dist_from(k: int):
        pque = []
        dist = [10 ** 9] * n
        dist[k] = 0
        heapq.heappush(pque, (0, k))
        while len(pque) > 0:
            now_cost, now = heapq.heappop(pque)
            if now_cost > dist[now]:
                continue
            for to, cost in graph[now]:
                if now_cost + cost < dist[to]:
                    dist[to] = now_cost + cost
                    heapq.heappush(pque, (now_cost + cost, to))
        return dist
    from_first = dist_from(0)  # 頂点 1 からの最短路長
    from_last = dist_from(n - 1)  # 頂点 N からの最短路長
    for i in range(n):
        print(from_first[i] + from_last[i])
if __name__ == "__main__":
    main()