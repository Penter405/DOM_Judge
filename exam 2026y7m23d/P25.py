from collections import defaultdict
talk=defaultdict(int)
be=defaultdict(int)
sc=defaultdict(int)
n,m=list(map(int,input().split()))
for _ in range(m):
    sub,obj=list(map(int,input().split()))
    talk[sub]+=1
    be[obj]+=1
    sc[sub]+=1
    sc[obj]-=1
result=[]
#print(be)
#print(sc)

t=0
n=0
ever=0
for rs in dict(be):
    name=rs
    times=be[rs]
    if ever==0:
        n=name
        t=times
        ever=1
        continue
    if times>t:
        n=name
        t=times
    elif times==t:
        if name<n:
            n=name
    
result.append(f"{n} {t}")
#--------
t=0
n=0
ever=0
for rs in dict(sc):
    name=rs
    times=sc[rs]
    if ever==0:
        n=name
        t=times
        ever=1
        continue
    if times>t:
        n=name
        t=times
    elif times==t:
        if name<n:
            n=name
    
result.append(f"{n} {t}")
print("\n".join(result))

"""
7 8
1 2
3 2
4 2
1 3
5 4
6 4
1 4
2 1
"""