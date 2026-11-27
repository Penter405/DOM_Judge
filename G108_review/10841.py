def dfs(node):
    global good
    if not good:
        return 0
    for child in point[node]:
        if color[child]==0:
            color[child]=(-1)*color[node]
            dfs(child)
        else:
            if color[child]==color[node]:
                good=False
for _ in range(int(input())):
    nodes=int(input())
    ways=int(input())
    point=[[] for _ in range(nodes)]
    color=[0 for _ in range(nodes)]
    color[0]=1
    for _ in range(ways):
        a,b=list(map(int,input().split()))
        point[a].append(b)
        point[b].append(a)

    good=True
    dfs(0)
    if good:
        print("T")
    else:
        print("F")