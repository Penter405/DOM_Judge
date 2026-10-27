from collections import defaultdict
nodes=int(input())
want=int(input())
parent=[n for n in range(nodes)]
point=defaultdict(list)
def find_root(n):
    if parent[n]!=n:
        return find_root(parent[n])
    return n
for _ in range(nodes-1):
    a,b=list(map(int,input().split(",")))
    point[b].append(a)
    parent[a]=b

root=find_root(0)

res=[]
def dfs(node=root,deep=0):
    global want
    #skip cheaking None
    if deep==want:
        res.append(node)

    for child in point[node]:
        dfs(child,deep+1)
dfs()
for rs in sorted(res):
    print(rs)
