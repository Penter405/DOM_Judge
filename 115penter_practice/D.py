"""
when past element bigger than you
when left element > right element
"""
sizeof=int(input())
d=list(map(int,input().split()))
d=d[::-1]
new=list(set(d))
new.sort()
place={
    k:(v+1) for v,k in enumerate(new)
}
ftree=[0]+[0]*len(new)
def add(ind,guy):
    while ind<len(ftree):
        ftree[ind]+=guy
        ind+=(ind&-ind)

def get(ind):
    res=0
    while ind>0:
        res+=ftree[ind]
        ind-=(ind&-ind)
    return res
res=0
for node in d:
    res+=get(place[node]-1)
    add(place[node],1)
print(res)