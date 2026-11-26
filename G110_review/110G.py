def get():
    return list(map(int,input().split()))
from collections import Counter
rule=get()
a=dict(Counter(rule))
have=list(dict(a).keys()).copy()
for _ in range(int(input())):
    me=get()
    b=dict(Counter(me))
    A=0
    for ind in range(4):
        if rule[ind]==me[ind]:
            A+=1
    B=0
    for h in have:
        B+=min(a.get(h,0),b.get(h,0))
    B-=A
    print("{}A{}B".format(A,B))
    