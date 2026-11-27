nodes, ways=list(map(int,input().split()))
point=[[] for _ in range(nodes+1)]
parent=[[] for _ in range(nodes+1)]
be=[0 for _ in range(nodes+1)]
for _ in range(ways):
    a,b=list(map(int,input().split()))
    point[a].append(b)
    parent[b].append(a)
    be[b]+=1
result=[0 for _ in range(nodes+1)]
nodes=set(list(range(1,nodes+1)))
while True:
    out=[]
    for node in nodes:
        if be[node]==0 and result[node]==0:
            if len(parent[node])==0:
                result[node]=1
            else:
                result[node]=max([result[p] for p in parent[node]])+1
            out.append(node)

    if len(out)==0:
        break
    for node in out:
        nodes.remove(node)
        for friend in point[node]:
            be[friend]-=1
if result.count(0)!=1:
    print(-1)
else:
    print(max(result))
    print(' '.join(list(map(str,result[1:]))))
