wx=input()
wy=input()
lx=len(wx)
ly=len(wy)
board=[[float('inf')]*(lx+1) for _ in range(ly+1)]
board[0][0]=0
for ind in range(lx+1):
    board[0][ind]=ind
for ind in range(ly+1):
    board[ind][0]=ind
for y in range(1,ly+1):
    for x in range(1,lx+1):
        if wx[x-1]==wy[y-1]:
            board[y][x]=min(board[y-1][x-1],board[y-1][x]+1,board[y][x-1]+1)
        else:
            board[y][x]=min(board[y-1][x-1],board[y-1][x],board[y][x-1])+1
print(board[-1][-1])
    