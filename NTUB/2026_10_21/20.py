from itertools import combinations
d=input()
d.replace(" ","")
d=list(map(int,d.split(",")))
res=set()
for rs in list(combinations(d,3)):
    res.add(sum(rs))

print(len(res))