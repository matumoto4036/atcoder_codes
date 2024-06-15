s=list(input())
t=list(input())
tmp=0
for i in s:
    tmp=t.index(i,tmp,len(t))+1
    print(tmp,end=" ")
    