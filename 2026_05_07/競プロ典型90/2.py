# N: int = int(input())

# candidate = []


# def dfs(S, f):
#     if f < 0:
#         return
#     if len(S) == N:
#         if f == 0:
#             candidate.append(S)
#         return

#     dfs(S + "(", f + 1)
#     dfs(S + ")", f - 1)
#     return


# if N % 2 == 0:
#     dfs("", 0)
# print(*candidate, sep="\n")

n=int(input())
ans=[]
def dfs(S,x):
    if x<0:return
    if len(S)==n:
        if x==0:
            ans.append(S)
        return
    dfs(S+"(",x+1)
    dfs(S+")",x-1)
    return

if n%2==0:dfs("",0)
ans.sort()
print(*ans,sep="\n")