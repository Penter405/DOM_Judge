from collections import defaultdict
n=int(input())
res=defaultdict(set)

for rs in range(n):
    nation,*guys=input().split()
    guys=" ".join(guys)
    res[nation].add(guys)

for key in sorted(dict(res).keys()):
    print(key,len(res[key]))
