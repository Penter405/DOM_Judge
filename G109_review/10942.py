path=[]
def dfs(node):
    global bad,t,cycle
    if went[node]:
        return 0
    t+=1
    went[node]=t
    next=point[node]
    if next==0:
        worth[node]=1
        return 0
    if went[next]:
        if worth[next]:
            worth[node]=worth[next]+1
            return 0
        else:
            bad=next
            cycle=went[node]-went[next]+1
            worth[node]=cycle

    else:
        dfs(next)
        if bad:
            worth[node]=cycle
            if node==bad:
                bad=0
                cycle=0
        else:
            worth[node]=worth[next]+1


for _ in range(int(input())):
    nodes=int(input())
    went=[0]*(nodes+1)
    worth=[0]*(nodes+1)
    point=[0]*(nodes+1)
    bad=0
    cycle=0
    t=0

    for _ in range(nodes):
        a,b=list(map(int,input().split()))
        point[a]=b



    for node in range(1,nodes+1):
        path.clear()
        dfs(node)
    good=0
    large=0
    for ind in range(1,len(worth)):
        if worth[ind]>large:
            large=worth[ind]
            good=ind
    print(good)
"""
3
3
1 2
2 3
3 1
4
1 2
2 1
4 3
3 2
5
1 2
2 1
5 3
3 4
4 5 

"""