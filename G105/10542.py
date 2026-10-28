import heapq
res=[]
guy=dict()
backtracking=[]
def dfs(n):
    #skip cheaking if self None
    if n not in point:
        guy[n]="".join(backtracking)

    else:
        if point[n][0]!=None:
            backtracking.append("0")
            dfs(point[n][0])
            backtracking.pop(-1)
        if point[n][1]!=None:
            backtracking.append("1")
            dfs(point[n][1])
            backtracking.pop(-1)


for _ in range(int(input())):
    d=list(map(int,input().split(",")))
    que=[]
    heapq.heapify(que)
    node=-1
    for rs in range(len(d)):
        node+=1
        heapq.heappush(que,(d[node],node))
    point=dict()
    while que:
        me_size,me=heapq.heappop(que)
        if len(que)==0:
            break
        friend_size,friend=heapq.heappop(que)
        node+=1
        point[node]=[friend,me]
        heapq.heappush(que,(me_size+friend_size,node))
    guy.clear()
    dfs(node)
    lres=["0"]*len(d)
    for ind in range(len(d)):
        lres[ind]=str(len(guy[ind]))
    res.append(",".join(lres))
    
        
for rs in res:
    print(rs)