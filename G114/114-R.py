import heapq
#from collections import 
#weighted bfs

y,x=list(map(int,input().split()))
board=[]
for a in range(y):
    board.append(list(map(int,input().split())))
arrive=[[0 for _ in range(x)]for _ in range(y)]

que=[]
heapq.heappush(que,(0,(0,0)))
def do():
    res=0
    while que:
        now,place=heapq.heappop(que)
        ny,nx=place
        if arrive[ny][nx]!=0:
            continue
        arrive[ny][nx]=now
        for a,b in [(1,0),(0,1)]:
            ay=ny+a
            ax=nx+b
            if ay>y-1 or ax>x-1:
                continue
            if ay==y-1 and ax==x-1:
                res=now+board[ay][ax]
                return res
            heapq.heappush(que,(now+board[ay][ax],(ay,ax)))
    return 0

print(do())
