from collections import defaultdict
nodes,ways=list(map(int,input().split()))
d=list(map(int,input().split()))
way=defaultdict(list)
for _ in range(ways):
    a,b=sorted(list(map(int,input().split())))
    way[a-1].append([b-1,_])
result=[-1]*ways
for a in list(dict(way).keys()):
    now=d[a]
    ind=a
    for b,_ in sorted(way[a]):
        while ind<b:
            ind+=1
            now=max(now,d[ind])
        result[_]=now

for line in result:
    print(line)