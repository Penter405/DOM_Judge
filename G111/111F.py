point=dict()
root=None
for _ in range(int(input())):
    a,b,c=list(map(int,input().split()))
    if root==None:
        root=a
    if a not in point:
        point[a]=[None,None]
    if b not in point:
            point[b]=[None,None]
    if c not in point:
        point[c]=[None,None]
    if b!=-1:
        point[a][0]=b
    if c!=-1:
        point[a][1]=c

res=dict()#ind:str
def dfs(node,pa=-1,dep=0):
    if node==None:
        return -1
    else:
        pass
    left=dfs(point[node][0],node,dep+1)
    right=dfs(point[node][1],node,dep+1)
    chi=0
    if left!=-1:
        chi+=1
    if right!=-1:
        chi+=1
    my_h=max(0,left+1,right+1)
    res[node]=f"node {node}: parent = {pa}, degree = {chi}, depth = {dep}, height = {my_h},"
    return my_h

dfs(root)
for rs in sorted(res.keys()):
    print(res[rs])

"""
9
0 1 4
1 2 3
2 -1 -1
3 -1 -1
4 5 8
5 6 7
6 -1 -1
7 -1 -1
8 -1 -1
"""