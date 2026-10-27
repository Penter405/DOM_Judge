
res=[]
def get():
    node=int(input())
    edge=int(input())
    point=[[] for _ in range(node)]
    color=[None]*node
    for _ in range(edge):
        a,b=list(map(int,input().split()))
        point[a].append(b)
        point[b].append(a)
    good=True
    def dfs(n=0,now=1):
        nonlocal good
        if not good:
            return 0
        if color[n]!=None:
            return 0
        color[n]=now
        for friend in point[n]:
            if color[friend]==now:
                good=False
            dfs(friend,-now)
    dfs()
    return good

for _ in range(int(input())):
    if get():
        res.append("T")
    else:
        res.append("F")

print("\n".join(res))