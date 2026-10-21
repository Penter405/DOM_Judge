from collections import defaultdict
point=defaultdict(list)
n=int(input())
for _ in range(n-1):
    a,b=list(map(int,input().split()))
    point[a].append(b)
    point[b].append(a)

ever=[False]*(n+1)
def postorder(n):
    if ever[n]:
        return 0
    ever[n]=True
    child=0
    for near in point[n]:
        child=max(child,postorder(near))

    return 1+child
res=[]
for rs in range(1,n+1):
    for pe in range(n+1):
        ever[pe]=False
    res.append(str(postorder(rs)-1))

print(" ".join(res))





