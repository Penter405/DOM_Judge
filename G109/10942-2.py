from collections import defaultdict
def solve():
    n=int(input())
    bepointed=[0]*(n+1)
    point=[0 for _ in range(n+1)]
    parent=[n for n in range(n+1)]
    for _ in range(n):
        root,child=list(map(int,input().split()))
        bepointed[child]+=1
        point[root]=child
        parent[child]=root

    in_cycle=[True]*(n+1);cycle_ind=[-1]*(n+1)
    cyleader=[]
    cyvalue=[]
    root=[]
    tail=[]
    tail_size=[]
    for ind in range(1,n+1):
        if not(in_cycle[ind]):
            continue
        if bepointed[ind]!=0:
            continue
        in_cycle[ind]=False
        root.append(ind)
        see=None;imtail=ind;imtail_size=1
        while True:
            if point[ind]==0:
                break
            see=point[ind]
            if bepointed[see]!=1:
                break
            bepointed[see]-=1
            imtail=see
            imtail_size+=1
            in_cycle[see]=False
        tail.append(imtail);tail_size.append(imtail_size)
    cyind=-1
    for ind in range(1,len(in_cycle)):
        if in_cycle[ind]:
            cyind+=1
            size=1
            begin=ind
            cyking=ind
            in_cycle[begin]=False
            cycle_ind[begin]=cyind
            see=ind
            while True:
                see=point[see]
                if see==begin:
                    break
                cyking=min(cyking,see)
                in_cycle[see]=False
                cycle_ind[see]=cyind
                size+=1
            cyvalue.append(size)
            cyleader.append(cyking)
    res=0
    best=0
    for t in range(len(tail)):
        friend=cyvalue[cycle_ind[point[tail[t]]]]
        now=tail_size[t]+friend
        if now>best:
            res=root[t]
        elif now==best:
            res=min(res,root[t])
    
    if res!=0:
        return res
    for rs in range(len(cyvalue)):
        if cyvalue[rs]>best:
            res=cyleader[rs]
            best=cyvalue[rs]
        elif cyvalue[rs]==best:
            res=min(res,cyleader[rs])
    return res
res=[]
for _ in range(int(input())):
    res.append(solve())

for rs in res:
    print(rs)


