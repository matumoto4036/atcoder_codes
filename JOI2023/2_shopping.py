N,M,Q=map(int, input().split())
p=[]
a=[]
t=[]
l=[]
r=[]
for i in range(N):
  tmp=list(map(int,input().split()))
  p.append(tmp[0])
  a.append(tmp[1])
for i in range(Q):
  tmp=list(map(int,input().split()))
  t.append(tmp[0])
  l.append(tmp[1]-1)
  r.append(tmp[2]-1)

for i in range(Q):
  sum=0
  for j in range(r[i]-l[i]+1):
    if t[i]==a[j+l[i]]:
      sum+=p[j+l[i]]//2
    else:
      sum+=p[j+l[i]]
  print(sum)

  '''
import bisect#二分探索
N, M, Q = map(int, input().split())
PA = [map(int, input().split()) for i in range(N)]
P, A = map(list, zip(*PA))#よく使えそう
A = [a - 1 for a in A]
S = [0] * (N + 1)
for i in range(N):
  S[i + 1] = S[i] + P[i]
idx = [[] for i in range(M)]
sum = [[0] for i in range(M)]
for i in range(N):
  idx[A[i]].append(i)
  sum[A[i]].append(sum[A[i]][-1] + P[i])
for i in range(Q):
  T, L, R = map(int, input().split())
  T = T - 1
  L = L - 1
  ans = S[R] - S[L]
  l = bisect.bisect_left(idx[T], L)
  r = bisect.bisect_left(idx[T], R)
  ans -= (sum[T][r] - sum[T][l]) // 2
  print(ans)
  '''