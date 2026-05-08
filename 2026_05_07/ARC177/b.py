n=int(input())
s=list(input())
ans=[]
c=0
flag="0"
for i in reversed(range(n)):
    if s[i]==flag :continue

    if flag=="0":
        ans.append("A"*(i+1))
        flag="1"
        c+=i+1
    elif flag=="1":
        ans.append("B"*(i+1))
        flag="0"
        c+=i+1
print(c)
print("".join(ans))
