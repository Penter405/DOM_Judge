"""
tree= nodes-1 == edge
"""
loop=[]
path=[]
pathset=set()
def dfs(n):
    global loop,path
    if loop:
        return 0
    if len(path)>=2 and n==path[-2]:
        return 0
    node[n]=1
    if n in pathset:
        loop=path[path.index(n):]
        return 0
    path.append(n);pathset.add(n)
    for child in point[n]:
        dfs(child)
    path.pop();pathset.remove(n)



for _ in range(int(input())):
    d=[list(map(int,a.split(","))) for a in input().split()]
    node=[-1]*21# -1 not a point, 0 a point, 1 visited
    point=[[] for _ in range(21)]
    for a,b in d:
        node[a]=0
        node[b]=0
        point[a].append(b)
        point[b].append(a)
    if node.count(0)-1==len(d):
        print("T")
    else:
        loop.clear()
        dfs(d[0][0])
        if len(loop):
            print(", ".join(list(map(str,sorted(loop)))))
        else:
            print("F")
