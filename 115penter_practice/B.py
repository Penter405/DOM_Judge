nodes, ths=list(map(int,input().split()))
d=list(map(int,input().split()))
occur=[None for _ in range(ths+1)]
ind=-1
did=0
res=float('inf')
for node in d:
    ind+=1
    if occur[node]==None:
        did+=1
    occur[node]=ind
    if did==ths:
        res=min(res,max(occur[1:])-min(occur[1:])+1)
if res==float('inf'):
    print(0)
else:
    print(res)