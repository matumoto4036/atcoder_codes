n=int(input())
s=input()
ans=0
c=0
if s.count("-")==0 or s.count("o")==0:
    print(-1)
    exit()
for i in range(n):
    if s[i]=="o":
        c+=1
    else:
        ans=max(ans,c)
        c=0
ans=max(ans,c)
print(ans)