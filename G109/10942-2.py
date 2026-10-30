from collections import deque
def solve():
    n=int(input())
    bepointed=[[] for _ in range(n+1)]
    point=[0 for _ in range(n+1)]
    parent=[n for n in range(n+1)]
    for _ in range(n):
        root,child=list(map(int,input().split()))
        bepointed[child].append(root)
        point[root]=child
        parent[child]=root

    #find cycle bridge
    endpoint=n
    walked=set()
    while True:
        if point[endpoint] in walked or point[endpoint]==0:
            break
        walked.add(endpoint)
        endpoint=point[endpoint]


    p=endpoint
    sizeof=set()
    while True:
        if p in sizeof:
            break
        sizeof.add(p)
        p=point[p]
    res=min(sizeof)
    large=len(sizeof)
    queue=deque()

        

    for rs in sizeof:
        queue.append((rs,len(sizeof)))
    while queue:
        n,get=queue.popleft()
        if get>large:
            large=get
            res=n
        elif get==large:
            res=min(res,n)
        for par in bepointed[n]:
            if par not in sizeof:
                queue.append((par,get+1))
    
    return res
res=[]
for _ in range(int(input())):
    res.append(str(solve()))

for rs in res:
    print(rs)

"""
1
5
1 2
2 3
3 1
4 5
5 4
"""    
"""
5
6
1 2
2 3
3 4
4 5
5 1
6 3
6
2 3
3 4
4 5
5 6
6 2
1 4
7
1 2
2 3
3 4
4 5
5 1
6 3
7 6
7
2 3
3 4
4 5
5 6
6 2
7 4
1 7
7
5 4
3 4
4 6
6 7
7 1
1 2
2 1
"""