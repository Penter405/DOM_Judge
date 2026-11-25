board=[]
value=[]
for _ in range(3):
    board.append(list(map(int,input().split())))
    value.append(sum(board[-1]))
target=sum(value)//2
for ind in range(3):
    board[ind][ind]=target-value[ind]
for line in board:
    print(*line)

