from collections import defaultdict,Counter
good=list(map(int,input().split()))
coun=dict(Counter(good))
result=[]
for _ in range(int(input())):
    a=0;b=0
    me=list(map(int,input().split()))
    got=defaultdict(int)
    for rs in range(4):
        if good[rs]==me[rs]:
            got[good[rs]]+=1
            a+=1
    coun2=dict(Counter(me))

    for rs in coun:
        if rs not in coun2:
            continue
        now=min(coun[rs],coun2[rs])
        now-=got[rs]
        b+=now
    result.append(f"{a}A{b}B")

print("\n".join(result))
