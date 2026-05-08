n=int(input())
sa=[0]
sb=[0]
apre=0
bpre=0
for i in range(n):
    ci,pi=map(int,input().split())
    if ci==1:apre+=pi
    else:bpre+=pi
    sa.append(apre)
    sb.append(bpre)
q=int(input())
for i in range(q):
    l,r=map(int,input().split())
    print(sa[r]-sa[l-1],end=" ")
    print(sb[r]-sb[l-1])
