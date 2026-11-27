import heapq
for _ in range(int(input())):
    que=[]
    gy=int(input())
    gx=int(input())
    board=[]
    for _ in range(gy):
        board.append(list(map(int,input().split())))

    heapq.heappush(que,(board[0][0],0,0))
    went=set()    
    while True:
        w,y,x=heapq.heappop(que)
        if (y,x) in went:
            continue
        went.add((y,x))
        if y+1==gy and x+1==gx:
            print(w)
            break
        for a,b in [[0,1],[0,-1],[1,0],[-1,0]]:
            ny=y+a
            nx=x+b
            if 0<=ny<gy and 0<=nx<gx:
                heapq.heappush(que,(w+board[ny][nx],ny,nx))
'''
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
'''