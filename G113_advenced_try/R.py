nodes=int(input())
visited=[False]*(nodes+1)
picked=[False]*(nodes+1)
point=[[] for _ in range(nodes+1)]
to_do=[]
be=[0]*(nodes+1)
for _ in range(nodes-1):
    a,b=list(map(int,input().split()))
    point[a].append(b)
    point[b].append(a)
    be[a]+=1
    be[b]+=1
result=0
any_1=True
while any_1:
    any_1=False
    to_do.clear()
    for index in range(len(be)):
        if be[index]==1:
            any_1=True
            to_do.append(index)

    for good in to_do:
        if not picked[good]:
            for neighbor in point[good]:
                if picked[neighbor]==False:
                    picked[good]==True
                    picked[neighbor]=True
                    result+=1
                    break
        for neighbor in point[good]:
            if be[neighbor]>0:
                be[neighbor]-=1
        be[good]=0


print(result)