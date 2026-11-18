from bisect import bisect_left
events=int(input())
d=[]
for _ in range(events):
    d.append(list(map(int,input().split())))

d.sort()
premax=[0]
value=[0]
for start,end in d:
    place=bisect_left(premax,start)
    if place>=len(premax):
        if value[-1]==1:
            premax[-1]=min(premax[-1],end)
        elif value[-1]==0:
            premax.append(end)
            value.append(1)
        continue
    if value[-1]==1:
        premax[-1]=min(premax[-1],end)
        continue
    if premax[place]>start:
        place-=1
    
        
    if value[place]<value[-1]:
        continue
    premax.append(end)
    value.append(value[place]+1)
print(value[-1])
