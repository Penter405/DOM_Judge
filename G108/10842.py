import heapq
def get():
    y=int(input())
    x=int(input())
    best=[[None for _ in range(x)] for _ in range(y)]

    board=[]
    for _ in range(y):
        board.append(list(map(int,input().split())))
    que=[(board[0][0],0,0)]
    best[0][0]=board[0][0]
    heapq.heapify(que)


    while que:
        w,yy,xx=heapq.heappop(que)
        if yy==y-1 and xx==x-1:
            return w
        for a,b in [[1,0],[-1,0],[0,1],[0,-1]]:
            ny=yy+a
            nx=xx+b
            if 0<=ny<y and 0<=nx<x and best[ny][nx]==None:
                best[ny][nx]=w+board[ny][nx]
                heapq.heappush(que, (w+board[ny][nx],ny,nx)  )
res=[]
for _ in range(int(input())):
    res.append(get())


for rs in res:
    print(rs)

"""

2
4
5
0 3 1 2 9
7 3 4 9 9
1 7 5 5 3
2 3 4 2 5
1
6
0 1 2 3 4 5 

"""