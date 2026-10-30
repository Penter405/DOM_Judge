from itertools import permutations
from collections import defaultdict
res=[]

for _ in range(int(input())):
    d,a,b=list(map(int,input().split(",")))
    d=sorted(list(permutations(str(d))))

    want=d[a-1]
    me=d[b-1]
    appearw=defaultdict(int)#want past did not used
    appearm=defaultdict(int)
    a=0
    b=0
    for rs in range(len(want)):
        if want[rs]==me[rs]:
            a+=1
            continue
        if appearw[me[rs]]>=1:
            b+=1
            appearw[me[rs]]-=1
        else:
            appearm[me[rs]]+=1
        if appearm[want[rs]]>=1:
            b+=1
            appearm[want[rs]]-=1
        else:
            appearw[want[rs]]+=1
    res.append(f"{a}A{b}B")

for rs in res:
    print(rs)