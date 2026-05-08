# import math
# xy=[list(map(int,input().split())) for _ in range(4)]
# for i in range(4):
#     r1 = math.atan2(xy[i][1] - xy[(i+3)%4][1], xy[i][0] - xy[(i+3)%4][0])
#     r2 = math.atan2(xy[(i+1)%4][1] - xy[i][1], xy[(i+1)%4][0] - xy[i][0])
#     if abs(180-r1+r2)%360<180:
#         print("Yes")
#         exit()
# print("No")

from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
# from atcoder.segtree import SegTree
# from atcoder.lazysegtree import LazySegTree
# from atcoder.dsu import DSU
from itertools import permutations, combinations
import math, heapq, sys
sys.setrecursionlimit(10**7)
_int = lambda x: int(x)-1
MOD = 998244353
INF = 1<<62
Yes, No = "Yes", "No"

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))

def calc(a, b, c, d):
    s = (a[0]-b[0])*(c[1]-a[1]) - (a[1]-b[1])*(c[0]-a[0])
    #(x0-x1)(y-y0)-(y0-y1)*(x-x0)
    '''
    '''
    t = (a[0]-b[0])*(d[1]-a[1]) - (a[1]-b[1])*(d[0]-a[0])
    return s*t < 0

ans = calc(a, c, b, d) and calc(b, d, a, c)
print(Yes if ans else No)
