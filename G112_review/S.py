nodes,edges=list(map(int,input().split()))

went=[False]*(nodes+1)
point=[[] for _ in range(nodes+1)]
status=True
def dfs(me):
    global status
    went[me]=True
    if len(point[me])!=2:
        status=False
    for friend in point[me]:
        if not went[friend]:
            dfs(friend)

for _ in range(edges):
    a,b=list(map(int,input().split()))
    point[a].append(b)
    point[b].append(a)


res=0
for node in range(1,nodes+1):
    if not went[node]:
        status=True
        dfs(node)
        if status:
            res+=1
print(res)
"""
17 15
1 8
1 12
5 11
11 9
9 15
15 5
4 13
3 13
4 3
10 16
7 10
16 7
14 3
14 4
17 6
"""