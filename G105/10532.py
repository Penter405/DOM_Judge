res=[]
post=[]
def dfs(n):
    #skip cheak self none
    for child in point[n]:
        if child==None:
            continue
        dfs(child)

    post.append(str(n))
for _ in range(int(input())):
    left_right=list(map(int,input().split(",")))
    appear_first=list(map(int,input().split(",")))
    lr=dict()#guy , index of left_right
    for rs in range(len(left_right)):
        lr[left_right[rs]]=rs
    root=appear_first[0]
    point=dict()
    point[root]=[None,None]
    for node in appear_first[1:]:
        point[node]=[None,None]
        see=root
        while True:
            if lr[node]<lr[see]:
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
    post.clear()
    dfs(root)
    res.append(",".join(post))

for rs in res:
    print(rs)


"""
2
4,2,5,1,6,7,3,8
1,2,4,5,3,7,6,8
6,3,1,7,4,0,2,8,5,9
0,1,3,6,4,7,2,5,8,9

"""