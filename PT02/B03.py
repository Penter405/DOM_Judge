from collections import defaultdict
"""
0  save  
1  parent
2  depth:self place
3  height:far from longest child  -> recursion in need
4  type: who are you, 3 option
5  children list
"""
def find_root(x):
    global find
    while True:
        if x not in find:
            return x
        x=find[x]
walk=defaultdict(list)
find={}
how_many=int(input())
for _ in range(how_many):
    bot=list(map(int,input().split()))
    for rs in range(bot[1]):
        walk[bot[0]].append(bot[rs+2])
        find[bot[rs+2]]=bot[0]
result=[[-2,-2,-2,-2,-2] for _ in range(how_many)]#by index of result
root=find_root(0)
#we do DFS, postorder, left right dont care
def big(a,b):
    if a>b:
        return a
    return b
def recursion(root,parent,depth):
    global result
    #print(root,parent,depth)
    max_child_depth=depth#for leaf, child depth==None, and self depth can be count, so return self depth
    for rs in walk[root]:
        max_child_depth=big(max_child_depth,recursion(rs,root,depth+1))
    result[root][0]=parent
    result[root][1]=depth
    result[root][2]=max_child_depth-depth
    bot=0
    if parent==-1:
        bot="root"
    elif len(walk[root])==0:
        bot="leaf"
    else:
        bot="internal node"
    result[root][3]=bot
    result[root][4]=walk[root]
    #print(result[root])
    return depth

recursion(root,-1,0)
#print(result)
#exit()
count=-1
for rs in result:
    count+=1
    print(f"node {count}: parent = {rs[0]}, depth = {rs[1]}, height = {rs[2]}, {rs[3]}, {rs[4]}")
"""
0  parent
1  depth:self place
2  height:far from longest child  -> recursion in need
3  type: who are you, 3 option
4  children list
"""