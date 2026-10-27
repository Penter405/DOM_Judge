from collections import defaultdict
d=input().replace("(","").replace(" ","").split(")")[:-1]
point=defaultdict(list)
parent=dict()
def find_root(n):
    if parent[n]!=n:
        return find_root(parent[n])
    return n

first_node=None
for data in d:
    p,c,status=data.split(",")
    p=int(p)
    c=int(c)
    if first_node==None:
        first_node=p
    point[p].append(c)
    if p not in parent:
        parent[p]=p
    parent[c]=p


root=find_root(first_node)
biggest=0
smallest=float("inf")
def dfs(node=root,deep=0):
    global biggest,smallest
    if node not in point:
        #it is a leaf
        biggest=max(biggest,deep)
        smallest=min(smallest,deep)

    for child in point[node]:
        dfs(child,deep+1)
dfs(root)

if biggest-smallest<=1:
    print(1)
else:
    print(0)
"""
(1,2,L)(1,3,R)(3,4,L)
"""