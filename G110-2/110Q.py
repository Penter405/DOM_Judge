import heapq
"""
marge 2 not min,  we will keep spend 2 not min
-> marge 2 min


"""
useless= input()
data=list(map(int,input().split()))
data.sort()

result=0

while data:
    if len(data)==1:
        break
    a=heapq.heappop(data)
    b=heapq.heappop(data)
    result+=a+b
    heapq.heappush(data,a+b)
print(result)