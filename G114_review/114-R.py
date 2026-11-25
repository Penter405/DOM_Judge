import heapq
y,x=list(map(int,input().split()))
board=[]
for _ in range(y):
    board.append(list(map(int,input().split())))

que=[]
heapq.heappush(que,(board[0][0],0,0))
went=set()
while que:
    w,my,mx=heapq.heappop(que)
    t=(my,mx)
    if t in went:
        continue
    went.add(t)
    for a,b in [[1,0],[0,1]]:
        ny=my+a
        nx=mx+b
        if ny==y-1 and nx==x-1:
            print(w)
            exit()
        if ny<y and nx<x:
            heapq.heappush(que,(w+board[ny][nx],ny,nx))
        