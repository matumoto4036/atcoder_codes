t=int(input())
res=[]
for i in range(t):
    ans=0
    a,b,c=map(int,input().split())
    if max(a,b)==c:
        zmin=10**(a-1)+10**(b-1)
        zmax=10**c-1
        zn=max(zmax-zmin+1,0)
        res.append(((zn*(zn+1))//2)%998244353)
    elif max(a,b)+1==c:
        tmp=min(a,b)
        tmpmin=10**(tmp-1)
        tmpmax=10**tmp-1
        aa=max(tmpmax-tmpmin+1,0)
        res.append((aa*(aa+1)//2)%998244353)
    else:res.append(0)

print(*res,sep="\n")

# t=int(input())
# res=[]
# for i in range(t):
#     ans=0
#     a,b,c=map(int,input().split())


#     if max(a,b)==c:
#         znum=(10**b-1-10**(a-1))-10**(b-1)+1
#         anum=10**a-1-10**(a-1)
#         zmin=znum-anum+1
#         res.append(((znum+zmin)*anum//2)%998244353)
#     elif max(a,b)+1==c:
#         tmp=min(a,b)
#         tmpmin=10**(tmp-1)
#         tmpmax=10**tmp-1
#         aa=max(tmpmax-tmpmin+1,0)
#         res.append((aa*(aa+1)//2)%998244353)
#     else:res.append(0)

# print(*res,sep="\n")
