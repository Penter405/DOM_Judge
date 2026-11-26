import heapq
big_at_0=[]#saves small data
small_at_0=[]#saves big data
sizeof=int(input())
def balance(data):
    global big_at_0, small_at_0
    #add inside first
    if len(big_at_0)==0:
        heapq.heappush_max(big_at_0,data)
    elif data>big_at_0[0]:
        heapq.heappush(small_at_0,data)
    else:
        heapq.heappush_max(big_at_0,data)
    
        

    while abs(len(big_at_0)-len(small_at_0))>1:
        while len(big_at_0)>len(small_at_0)+1:
            target=heapq.heappop_max(big_at_0)
            heapq.heappush(small_at_0,target)
        while len(small_at_0)>len(big_at_0)+1:
            target=heapq.heappop(small_at_0)
            heapq.heappush_max(big_at_0,target)

for _ in range(sizeof):
    d=int(input())
    balance(d)

    did=_+1
    if did%2==0:
        print((big_at_0[0]+small_at_0[0])//2)
    elif len(big_at_0)>len(small_at_0):
        print(big_at_0[0])
    else:
        print(small_at_0[0])