n=int(input())
have=[]
ans=[]
for i in range(n):
    a,c=map(int,input().split())
    if i==0:
        have.append([a,c])
        ans.append(i)
        continue
        
    tmp=ans[-1]
    de=[]
    for j in ans:
        if have[j][0]<a and have[j][1]>c:
            de.append(j)
        if have[j][0]>a and have[j][1]<c:break
        if j==tmp:
            ans.append(i)
            break
    for j in de:ans.pop(ans.index(j))
    have.append([a,c])
print(len(ans))
for i in range(len(ans)):
    print(ans[i]+1,end=" ")
