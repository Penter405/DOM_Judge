import heapq
for _ in range(int(input())):
    que=[]
    nodes,ways=list(map(int,input().split()))
    went=set()
    point=[[] for _ in range(nodes)]
    now_cost=0
    for _ in range(ways):
        a,b,w=list(map(int,input().split()))
        now_cost+=w
        point[a].append((w,b))
        point[b].append((w,a))
    #do prim
    new_cost=0
    heapq.heappush(que,(0,0))
    while len(went)<nodes:
        w,node=heapq.heappop(que)
        if node in went:
            continue
        went.add(node)
        new_cost+=w
        for nw,child in point[node]:
            if child in went:
                continue
            heapq.heappush(que,(nw,child))
    print(now_cost-new_cost)
"""
1
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11
"""
"""
3
7 11
0 1 7
0 3 5
1 2 8
1 3 9
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11
3 3
0 1 5
1 2 5
2 0 10
4 3
0 1 5
1 2 5
2 3 5
"""