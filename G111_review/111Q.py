import heapq
sizeof=int(input())
d=list(map(int,input().split()))
heapq.heapify(d)
res=0
while len(d)!=1:
    now=(heapq.heappop(d)+heapq.heappop(d))
    res+=now
    heapq.heappush(d,now)
print(res)