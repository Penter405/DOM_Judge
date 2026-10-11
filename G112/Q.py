import heapq
res=[]
while True:
    x=int(input())
    if x==0:
        break
    d=list(map(int,input().split()))
    heapq.heapify(d)
    ans=0
    while len(d)!=1:
        a=heapq.heappop(d)
        b=heapq.heappop(d)
        ans+=a+b
        heapq.heappush(d,a+b)
    res.append(str(ans))

    

print("\n".join(res))
"""
3
1 2 3
4
1 2 3 4
0

"""