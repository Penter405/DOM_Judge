d=[]
for _ in range(int(input())):
    d.append(int(input()))


for rs in d:
    board=[[0 for _ in range(rs)] for _ in range(rs)]
    plus=0
    for _ in range(rs):
        y=_
        x=0
        while True:
            plus+=1
            board[y][x]=plus
            if y==0:
                break
            x+=1
            y-=1
    space=len(str(plus))
    y=-1
    for rs in range(rs,0,-1):
        y+=1
        for x in range(rs):
            if x==rs-1:
                print(str(board[y][x]).zfill(space))
            else:
                print(str(board[y][x]).zfill(space),end=" ")