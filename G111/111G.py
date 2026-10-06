"""
inorder= on left or right
preorder=who on top
"""
def postorder(node):
    if node==None:
        return 0
    postorder(point[node][0])
    postorder(point[node][1])
    ans.append(node)
    return 0
res=[]
while True:
    try:
        d=input()
    except:
        break
    pre,ino=d.split()
    point=dict()
    place=dict()
    ans=[]
    for rs in range(len(ino)):
        place[ino[rs]]=rs
    root=None
    for node in pre:
        point[node]=[None,None]
        if root==None:
            root=node
            continue
        see=root

        while True:
            if place[node]<place[see]:
                if point[see][0]==None:
                    point[see][0]=node
                    break
                else:
                    see=point[see][0]
            else:
                if point[see][1]==None:
                    point[see][1]=node
                    break
                else:
                    see=point[see][1]
    postorder(root)
    res.append("".join(ans))

print("\n".join(res))
"""
DBACEGF ABCDEFG
BCAD CBAD
"""