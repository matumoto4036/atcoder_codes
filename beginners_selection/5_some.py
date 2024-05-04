n,a,b=map(int,input().split())
c=0
for i in range(n+1):
    tmp=0
    s=list(str(i))
    for j in range(len(s)):
        tmp+=int(s[j])
    if a<=tmp<=b:
        c+=i
print(c)