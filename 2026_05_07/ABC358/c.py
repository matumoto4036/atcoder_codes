n,m=map(int,input().split())
c=[]
s=[]
for i in range(n):
    tmp=str(input())
    s.append(tmp)
    c.append(tmp.count("o"))

def check(a,b):
    ans=0
    for i in range(len(a)):
        if a[i]=="o" and b[i]=="x":
            ans+=1
    return ans

ac=["x"]*m
l=0
while not ac.count("o")==m:
    store=-1
    max=0
    for i in range(n):
        tmp=check(s[i],ac)       
        if max<tmp:
            store=i
            max=tmp
    for i in range(m):
        if s[store][i]=="o":
            ac[i]="o"
    l+=1
print(l)

