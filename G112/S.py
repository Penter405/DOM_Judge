from collections import defaultdict
res=0
n,m=list(map(int,input().split()))
parent=[rs for rs in range(n+1)]
point=[0 for _ in range(n+1)]
def find(n):
    if parent[n]!=n:
        return find(parent[n])
    return n
def marge(a,b):
    parent[b]=a

king=defaultdict(list)
for rs in range(m):
    a,b=list(map(int,input().split()))
    point[a]+=1
    point[b]+=1
    marge(find(a),find(b))


for rs in range(1,n+1):
    king[find(rs)].append(rs)

for rs in king:
    good=True
    for child in king[rs]:
        if point[child]!=2:
            good=False
            break
    if good:
        res+=1

print(res)

"""
5 4
1 2
3 4
5 4
3 5
"""