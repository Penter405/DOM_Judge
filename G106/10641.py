from collections import defaultdict
def solve():
    is_loop=False
    d=input().split()
    botd=[]
    for rs in d:
        rs=rs.split(",")
        botd.append(int(rs[0]));botd.append(int(rs[1]))
    d=botd#reference
    app=set(d)
    parent=[]
    for rs in range(21):
        if rs not in app:
            me=-1
        else:
            me=rs
        parent.append(me)
    def find(n):
        nonlocal parent
        if parent[n]!=n:
            return find(parent[n])
        return n
    def marge(a,b):
        nonlocal parent
        ra=find(a)
        rb=find(b)
        parent[rb]=ra
    did=False
    def dfs(n):
        nonlocal bepoint, parent, did
        if bepoint[n]!=1:
            return 0
        bepoint[n]=0
        for child in point[n]:
            if bepoint[child]!=0:
                bepoint[child]-=1
        for child in point[n]:
            dfs(child)
        

    
    point=defaultdict(list)
    bepoint=defaultdict(int)
    for rs in range(0,len(d),2):
        a=d[rs]
        b=d[rs+1]
        point[a].append(b)
        point[b].append(a)
        bepoint[a]+=1
        bepoint[b]+=1
        if is_loop:
            continue
        ar=find(a);br=find(b)
        
        if ar==br:
            is_loop=True
        marge(a,b)




    if is_loop:
        for rs in range(21):
            if bepoint[rs]!=1:
                continue
            dfs(rs)
        res=[]
        for rs in range(21):
            if bepoint[rs]!=0:
                res.append(str(rs))
        return ", ".join(res)
    else:
        if len(app)-1==len(d)//2:
            return "T"
        else:
            return "F"
res=[]
for _ in range(int(input())):
    res.append(str(solve()))

for rs in res:
    print(rs)
"""
0, 2, 6, 8 
5
1,2 2,3 4,0
4,3 2,3 2,1 1,0
1,2 2,3 3,4 1,4 1,5
1,2 1,3 2,3
1,2 2,3 3,4 1,5 5,4

1
4,3 2,3 2,1 1,0


4
5,8 5,3 5,2 5,4 5,6 1,2 2,0
8,1 1,3 6,2 8,10 7,5 1,4 7,8 8,6 8,0
3,8 6,8 6,4 0,6 8,2 2,0 5,3
1,0 4,3 1,2

1
3,8 6,8 6,4 0,6 8,2 2,0 5,3
"""