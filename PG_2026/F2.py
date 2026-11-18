persons, helpme=list(map(int,input().split()))
point=[[] for _ in range(persons+1)]
went=[False]*(persons+1)
for _ in range(persons-1):
    a,b=list(map(int,input().split()))
    point[a].append(b)
    point[b].append(a)
large=0
guy=0
def dfs(n,depth=0):
    global large,guy
    if went[n]:
        return 0
    went[n]=True
    if depth>large:
        guy=n
        large=depth
    elif depth==large:
        if n<guy:
            guy=n
    for child in point[n]:
        dfs(child,depth+1)
    return 0
dfs(helpme)
print(guy,large)