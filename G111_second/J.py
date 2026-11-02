res=[]
def dfs(n,guy,length=1):
    global board
    res=0
    for child in point[guy]:
        if board[n][child]==0 and n!=child:
            board[n][child]=length
            res+=length
            res+=dfs(n,child,length+1)
    return res
for _ in range(int(input())):
    edge=eval(input())
    board=[[0 for _ in range(len(edge)+1)] for _ in range(len(edge)+1)]
    point=[[] for _ in range(len(edge)+1)]
    for rs in edge:
        a,b=sorted(rs)        
        point[a].append(b)
        point[b].append(a)
    plus=0
    for main_ind in range(len(edge)+1):
        plus+=dfs(main_ind,main_ind)

    res.append(str(plus))

for rs in res:
    print(rs)

