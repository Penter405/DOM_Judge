longest=0
good=0
n=int(input())
point=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b=list(map(int,input().split()))
    point[a].append(b)
    point[b].append(a)


def dfs(node=1,depth=0,parent=None):
    global longest, good
    if depth>longest:
        longest=depth
        good=node
    for child in point[node]:
        if parent==None or parent!=child:
            dfs(child,depth+1,node)
dfs()
longest=0
root=good
good=0
dfs(root)
print(longest)
"""
10
2 1
3 1
4 3
5 4
6 5
7 1
8 6
9 2
10 6
"""