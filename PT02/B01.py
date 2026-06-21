from collections import defaultdict,deque
walk=defaultdict(list)
bfs_line=deque()
bfs_result=[]
dfs_result=[]
default=list(map(int,input().split()))
for rs in range(default[0]-1):
    bot=list(map(int,input().split()))
    walk[bot[0]].append(bot[1])
def bfs(root:int):
    global bfs_line
    bfs_line.append(root)
    while bfs_line:
        me=bfs_line.popleft()
        bfs_result.append(str(me))
        for rs in sorted(walk[me]):
            bfs_line.append(rs)
        



def dfs(root:int):
    dfs_result.append(str(root))
    for rs in sorted(walk[root]):
        dfs(rs)
bfs(default[1])
dfs(default[1])
print(" ".join(bfs_result))
print(" ".join(dfs_result))

