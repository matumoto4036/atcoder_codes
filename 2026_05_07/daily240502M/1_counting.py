# n=int(input())
# la=[list(map(int,input().split())) for _ in range(n)]
# c=0
# for i in range(n-1):
#     for j in range(i+1,n):
#         if la[i]==la[j]:
#             c+=1
# print(n-c)

# n=int(input())
# la=[]
# c=0
# for i in range(n):
#     a=list(map(int,input().split()))
#     la.append()
#     if i==0:
#         continue
#     for j in range(i):
#         if la[i]==la[j]:
#             c+=1
# print(n-c)

N = int(input().strip())
st = set()
for _ in range(N):
	st.add(tuple(map(int, input().strip().split())))
print(len(st))