from collections import defaultdict
point=defaultdict(list)
belong=dict()
a=None
for _ in range(int(input())-1):
    parent,child=input().split()
    if a==None:
        a=int(parent)
    parent=int(parent)
    child=int(child)
    point[parent].append(child)
    if parent not in belong:
        belong[parent]=parent
    belong[child]=parent


def find(n):
    if belong[n]!=n:
        return find(belong[n])
    return n

root=find(a)
res=[]
def dfs(n):
    res.append(str(n))
    for child in sorted(point[n]):
        dfs(child)
dfs(root)
print(" ".join(res))