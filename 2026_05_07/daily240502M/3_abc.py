# import math
# n=int(input())
# ans=0
# for a in range(1,int(math.pow(n,1/3))+1):
#     for b in range(a,int(math.pow(n,1/2))+1):
#         for c in range(b,n):
#             if a*b*c<=n:
#                 ans+=1
#             else:
#                 break
#     else:
#         continue
# print(ans)

N=int(input())
ans=0
for a in range(1,N+1):
	if a*a*a>N: break
	for b in range(a,N+1):
		if a*b*b>N: break
		ans+=N//a//b-b+1
print(ans)