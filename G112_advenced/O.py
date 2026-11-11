import math
from sys import stdin
d=stdin.read().split("\n")[:-1]
res=[]
for line in d:
    begin_team,want_day=list(map(int,line.split()))
    r=begin_team-1
    b=((1+r)*r)//2
    n=want_day
    pen=(n+b)*2
    ans=int((-1 +  math.sqrt(1+4*pen))//2)

    while ans*ans+ans <pen:
        ans+=1
    res.append(ans)

for rs in res:
    print(rs)
