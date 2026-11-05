from collections import defaultdict
from sys import stdin
res=[]
d=stdin.read().replace("\n","").split("()")
if d[-1]=="":
    d.pop(-1)
def dfs(me=""):
    if me not in place:
        return 0
    layer[len(me)].append(str(place[me]))
    place.pop(me)
    dfs(me+"L")
    dfs(me+"R")
for edges in d:
    if len(edges)==edges.count(" "):
        print("not complete")
        continue
    res.clear()
    layer=defaultdict(list)
    place=dict()
    appear=set()
    bad=False
    for edge in edges.replace("(","").split(")")[:-1]:
        a,b=edge.replace(" ","").split(",")
        if b in place:
            bad=True
        place[b]=a
    if not bad:
        dfs()
    if bad or len(place)>0:
        print("not complete")
    else:
        x=-1
        while True:
            x+=1
            if x not in layer:
                break
            for update in layer[x]:
                res.append(update)
        print(" ".join(res))
"""
5  4 11  7  2  8  13  4  1
"""
"""
(42,) ()
()
"""