import math
res=[]
for _ in range(int(input())):
    d=list(map(int,input().split(",")))
    best=1
    for a in range(len(d)):
        for b in range(a+1,len(d)):
            best=max(best,math.gcd(d[a],d[b]))
    res.append(best)

for rs in res:
    print(rs)