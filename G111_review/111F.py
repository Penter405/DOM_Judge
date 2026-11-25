n=int(input())
point=[[] for _ in range(n)]
parent=[-1 for _ in range(n)]
for _ in range(n):
    node,a,b=list(map(int,input().split()))
    point[node]=(a,b)
    parent[a]=node
    parent[b]=node

root=0
while parent[root]!=-1:
    root=parent[root]
res=['' for _ in range(n)]
def dfs(node, parent=-1 ,depth=0):
    childs=0
    long=0
    for child in point[node]:
        if child!=-1:
            childs+=1
            long=max(long,dfs(child,node,depth+1))
    res[node]=f"node {node}: parent = {parent}, degree = {childs}, depth = {depth}, height = {long}"
    return 1+long
dfs(root)
for line in res:
    print(line+',')
"""
9
0 1 4
1 2 3
2 -1 -1
3 -1 -1
4 5 8
5 6 7
6 -1 -1
7 -1 -1
8 -1 -1
"""