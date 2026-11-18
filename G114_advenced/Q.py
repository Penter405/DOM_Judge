from sys import stdin
for line in stdin.read().split("\n")[:-1]:
    top_down, lr=line.split()
    if len(top_down)==0:
        print("")
        continue
    place=dict()
    index=-1
    for element in lr:
        index+=1
        place[element]=index


    postorder=[]
    parent=dict()
    point=dict()
    root=top_down[0]
    point[root]=[None,None]
    for node in top_down[1:]:
        see=root
        point[node]=[None,None]
        while True:
            if place[see]<place[node]:
                if point[see][1]==None:
                    point[see][1]=node
                    break
                else:
                    see=point[see][1]
            else:
                if point[see][0]==None:
                    point[see][0]=node
                    break
                else:
                    see=point[see][0]
    def post(n):
        if n==None:
            return 0
        for child in point[n]:
            post(child)
        postorder.append(str(n))
    post(root)

    print("".join(postorder))

"""
DBACEGF ABCDEFG
BCAD CBAD
"""