node,edges=list(map(int,input().split()))
edge=[]
parent=[0]+[n for n in range(1,node+1)]
bepoint=[0]+[0]*node
def find(n):
    if n!=parent[n]:
        return find(parent[n])
    return n
def marge(a,b):
    ar=find(a)
    br=find(b)
    parent[ar]=br
for _ in range(edges):
    a,b=list(map(int,input().split()))
    bepoint[a]+=1
    bepoint[b]+=1
    marge(a,b)
imgood={}
roots=[]
for rs in range(1,len(parent)):
    if rs==parent[rs]:
        roots.append(rs)
for rs in roots:
    imgood[rs]=True

for rs in range(1,len(parent)):
    if bepoint[rs]!=2:
        imgood[find(rs)]=False

print(list(imgood.values()).count(True))