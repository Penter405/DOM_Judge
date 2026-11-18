phones, edges, k=list(map(int,input().split()))
phone=list(map(int,input().split()))


parent=[0]+[0]*phones
has=[0]+[0]*phones
for index in range(phones):
    if phone[index]:
        parent[index+1]=index+1
        has[index+1]=1

def find(me):
    if me!=parent[me]:
        return find(parent[me])
    return me

def marge(a,b):
    ra=find(a)
    rb=find(b)
    parent[rb]=ra#ra is new king
    has[ra]+=has[rb]

for _ in range(edges):
    a,b=list(map(int,input().split()))
    if parent[a]==0 or parent[b]==0:
        continue
    marge(a,b)
legals=0
best=0
for index in range(1,phones+1):
    if parent[index]==index:
        if has[index]>=k:
            legals+=1
            best=max(best,has[index])

print(legals,best)