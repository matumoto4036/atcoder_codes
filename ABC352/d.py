n,k=map(int,input().split())
p=list(map(int,input().split()))
minm=2*10e5

import itertools
items=[i+1 for i in range(n)]
comb = itertools.combinations(items, k)
for j in comb:
    s=[]
    for l in range(k):
        s.append(p[j[l]-1])
    s.sort()
    if (s[len(s)-1]-s[0])==len(s)-1:
        minm=min(minm,s[len(s)-1]-s[0])
print(minm)




# s.append(p[i])
# p[j]
# s.sort()
# if (s[len-1]-s[0])==len(s)-1:
#   print(2)


# from atcoder.segtree import SegTree

# N, K = map(int, input().split())
# P = list(map(int, input().split()))

# l = [0] * N
# for i in range(N):
#     l[P[i]-1] = i

# seg_min = SegTree(min, 10**9, l)
# seg_max = SegTree(max, 0, l)

# ans = 10**9
# for i in range(N-K+1):
#     ans = min(ans, seg_max.prod(i, i+K) - seg_min.prod(i, i+K))
# print(ans)