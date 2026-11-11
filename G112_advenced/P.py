#from collections import defaultdict
import heapq
sizeof=int(input())
node=[(amount,index) for index,amount in enumerate(list(map(int,input().split())))]
que=node.copy()
heapq.heapify(que)
point=dict()
for i in range(sizeof-1):
    i+=sizeof
    am,ai=heapq.heappop(que)
    bm,bi=heapq.heappop(que)#m == result
    point[i]=[ai,bi]
    heapq.heappush(que,(am+bm,i))
#print(list(que))
root=(sizeof-1)*2
result=0
def dfs(node,depth=0):
    global result
    if node not in point:
        result+=depth
        return 0
    for child in point[node]:
        dfs(child,depth+1)
    return 0

dfs(root)
print(result)
"""
7
2 3 6 8 13 15 19
"""