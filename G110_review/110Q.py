import heapq
sizeof=int(input())
que=list(map(int,input().split()))
heapq.heapify(que)
res=0
while len(que)>1:
    now=heapq.heappop(que)+heapq.heappop(que)
    res+=now
    heapq.heappush(que,now)
print(res)