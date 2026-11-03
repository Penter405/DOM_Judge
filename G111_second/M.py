import heapq
res=[]

for _ in range(int(input())):
    y=int(input())
    x=int(input())
    board=[]
    for _ in range(y):
        board.append(list(map(int,input().split())))
    went=[[False for _ in range(len(board[0]))] for _ in range(len(board))]
    que=[]
    heapq.heappush(que,(-board[0][0],0,0,board[0][0]))
    while True:
        w,my,mx,minw=heapq.heappop(que)
        if went[my][mx]:
            continue
        went[my][mx]=True
        if my+1==y and mx+1==x:
            res.append(minw)
            break

        for a,b in [[1,0],[-1,0],[0,1],[0,-1]]:
            if 0<=my+a<y and 0<=mx+b<x and (not went[my+a][mx+b]):
                heapq.heappush(que,(-board[my+a][mx+b],my+a,mx+b,min(minw,board[my+a][mx+b])))
                

for rs in res:
    print(rs)
