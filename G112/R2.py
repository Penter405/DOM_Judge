n=int(input())
point=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b=list(map(int,input().split()))
    point[a].append(b)
    point[b].append(a)
farest=None
distance=0
root_depth=1
visit=[False]*(n+1)
def dfs(node=1,depth=1):
    global farest,distance,root_depth
    if visit[node]:
        return 0
    visit[node]=True
    if depth-root_depth>distance:
        farest=node
        distance=depth-root_depth
    for child in point[node]:
        dfs(child,depth+1)
    return 0

dfs()
visit=[False]*(n+1)
dfs(farest)
print(distance)
"""
5
1 2
1 3
3 4
3 5
"""