from collections import defaultdict
ds, ways=list(map(int,input().split()))
d=list(map(int,input().split()))
way=[]
for _ in range(ways):
    a,b=list(map(int,input().split()))
    way.append([a-1,b-1,_])
spl=int(ds**0.5)+1
way.sort(key= lambda x:(x[0]//spl,x[1]))
result=[0]*ways
na=0
nb=-1
now=defaultdict(int)
for wa,wb,_ in way:
    if wb<nb:
        na=wa
        nb=na-1
        now.clear()
    while nb<wb:
        nb+=1
        now[d[nb]]+=1

    while na<wa:
        now[d[na]]-=1
        na+=1
    while na>wa:
        na-=1
        now[d[na]]+=1
    tar=list(now.values())
    result[_]=len(tar)-tar.count(0)

for line in result:
    print(line)
