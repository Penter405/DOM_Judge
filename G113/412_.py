#1 indexed
from collections import defaultdict
d, ranges=list(map(int,input().split()))
nums=list(map(int,input().split()))
place=[[]for _ in range(d+2)]
for a in range(ranges):
    st,en=list(map(int,input().split()))
    place[st].append(a)
    place[en+1].append(a)
ever=False
need=[False]*ranges
count=[set() for _ in range(ranges)]
ind=0
for n in nums:
    ind+=1
    for guy in place[ind]:
        if len(need)!=0:
            ever=True
        need[guy]=not(need[guy])
    do=False
    for rs in range(ranges):
        if need[rs]:
            count[rs].add(n)
            do=True
            ever=True
    if ever and not do:
        break

for rs in count:
    print(len(rs))
"""
5 3
3 2 3 1 2
1 3
2 4
1 5

"""
