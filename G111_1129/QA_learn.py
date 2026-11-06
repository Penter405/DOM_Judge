from collections import defaultdict
from sys import stdin
d=stdin.read().split("\n")
for line in d:
    if line=="":
        continue
    times=defaultdict(int)
    d=list(map(int,line.split(",")))
    res=0
    times[d[0]]+=1
    for rs in d[1:]:
        res+=times[rs]
        times[rs]+=1
    print(res)