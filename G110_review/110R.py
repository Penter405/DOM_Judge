nodes,ways=list(map(int,input().split()))
point=[[] for _ in range(nodes+1)]
for _ in range(ways):
    a,b=list(map(int,input().split()))
    point[a].append(b)

a,b=list(map(int,input().split()))
went=[False]*(nodes+1)
def dfs(a):
    if went[a]:
        return 0
    went[a]=True
    for child in point[a]:
        if not went[child]:
            dfs(child)
    return 0
dfs(a)

if went[b]==True:
    print('Yes')
else:
    print('No')