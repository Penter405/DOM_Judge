#b tree
#tree pick up, and no point in two match

your_options=[]
this_time=0
visit2=set()
def dfs2(root,n,depth=0):
    global this_time
    if visited[n]==False:
        return 0
    if n in visit2:
        return 0
    visit2.add(n)
    if depth==2:
        if visited[n]:
            your_options.append(n)
        return 0
    if depth==1 and visited[n]:
        this_time=1
    for child in point[n]:
        if child!=root:
            dfs2(root,child,depth+1)

def dfs(guy):
    global visited,this_time
    if visited[guy]:
        return 0
    visited[guy]=True
    this_time=0
    your_options.clear()
    visit2.clear()
    dfs2(guy,guy)
    must_choose_me[guy]=this_time+max([0]+[must_choose_me[option] for option in your_options])
    for child in point[guy]:
        dfs(child)
    return 0



nodes=int(input())
visited=[False]*(nodes+1)
must_choose_me=[0]*(nodes+1)
point=[[] for _ in range(nodes+1)]
be=[0]*(nodes+1)
for _ in range(nodes-1):
    a,b=list(map(int,input().split()))
    point[a].append(b)
    point[b].append(a)
    be[a]+=1
    be[b]+=1
begin=None
for index in range(len(be)):
    if be[index]==1:
        begin=index
dfs(begin)
print(max(must_choose_me))