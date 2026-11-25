y,x=list(map(int,input().split()))
board=[]
for _ in range(y):
    board.append(input().split())

board=zip(*(board))
for line in board:
    print(" ".join(line))