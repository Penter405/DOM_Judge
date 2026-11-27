import heapq
nodes,ways=list(map(int,input().split()))
d=list(map(int,input().split()))
part=int(nodes**0.5)+1
way=[]
for _ in range(ways):
    a,b=sorted(list(map(int,input().split())))
    way.append([a-1,b-1,_])
result=[-1]*ways
now=[]
way.sort(key= lambda x:(x[0]//part,x[1]))
l=0
r=-1
for wantl,wantr,resind in way:
    if wantr<r:
        l=wantl
        r=l-1
        now.clear()
    while r<wantr:
        r+=1
        heapq.heappush_max(now,d[r])
    while l<wantl:
        now.remove(d[l])
        l+=1

    while l>wantl:
        l-=1
        heapq.heappush_max(now,d[l])
    
    result[resind]=now[0]

for line in result:
    print(line)