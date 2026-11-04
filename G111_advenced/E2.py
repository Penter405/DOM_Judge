import heapq
res=[]
for _ in range(int(input())):
    que=[]
    board=[]
    y=int(input())
    x=int(input())
    for _ in range(y):
        board.append(list(map(int,input().split())))

    heapq.heappush(que,(board[0][0],0,0))
    went=set()
    while que:
        w,my,mx=heapq.heappop(que)
        if mx+1==x and my+1==y:
            res.append(w)
            break
        if (my,mx) in went:
            continue
        went.add((my,mx))
        
        for a,b in [[1,0],[-1,0],[0,1],[0,-1]]:
            nx=mx+a
            ny=my+b
            if 0<=nx<x and 0<=ny<y:
                heapq.heappush(que,(w+board[ny][nx],ny,nx))

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



3
1
1
9
2
2
0 0
0 0
5
6
0 9 9 0 0 0
0 9 0 0 9 0
0 9 0 9 9 0
0 0 0 9 9 0
9 9 9 9 9 0
"""