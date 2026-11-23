from collections import defaultdict
d_size,interval_size=list(map(int,input().split()))
d=list(map(int,input().split()))
interval=[]
result=[0]*interval_size
part=int(d_size**0.5)
for _ in range(interval_size):
    a,b=list(map(int,input().split()))
    a-=1;b-=1
    interval.append([a,b,_])


interval.sort(key=lambda x:(x[0]//part,x[1]))
left=0
right=-1
now=defaultdict(int)
for a,b, index in interval:
    if a==3 and b==4:
        print("target")
    #moving point to current place
    if b<right:
        now.clear()
        left=a
        right=a-1
    while b!=right:
        right+=1
        now[d[right]]+=1

    while a>left:
        now[d[left]]-=1
        left+=1
    while a<left:
        left-=1
        now[d[left]]+=1
    result[index]=len(now.values())-list(now.values()).count(0)

for rs in result:
    print(rs)