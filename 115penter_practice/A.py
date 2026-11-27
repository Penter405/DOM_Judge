from collections import defaultdict
d=defaultdict(int)
for _ in range(int(input())):
    a,b=list(map(int,input().split()))
    d[a]+=1
    d[b]-=1
res=0
now=0
start=None
for k in sorted(list(dict(d).keys())):
    now+=d[k]
    if now>0:
        if start==None:
            start=k
    elif now==0:
        res+=k-start
        start=None
print(res)
