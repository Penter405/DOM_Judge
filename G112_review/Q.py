import heapq
while True:
    sizeof=int(input())
    if sizeof==0:
        exit()
    que=list(map(int,input().split()))
    heapq.heapify(que)
    res=0
    while len(que)!=1:
        now=heapq.heappop(que)+heapq.heappop(que)
        res+=now
        heapq.heappush(que,now)
    print(res)
"""
3
1 2 3
4
1 2 3 4
0
"""