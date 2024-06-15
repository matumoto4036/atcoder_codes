'''
2 2000 500 NSK種類 条件 送料 
1000 1 PQ価格 個数
100 6'''
# n,s,k=map(int,input().split())
# pq=[list(map(int,input().split())) for _ in range(n)]
# #p,q=map(list,zip(*pq))
# ans=0
# for i in range(n):
#     ans+=pq[i][0]*pq[i][1]
# if ans<s:
#     ans+=k
# print(ans)

n,s,k=map(int,input().split())
ans=0
for i in range(n):
    p,q=map(int,input().split())
    ans+=p*q
if ans<s:
    ans+=k
print(ans)