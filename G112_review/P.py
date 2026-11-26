board=[]
value=[]
for _ in range(3):
    now=list(map(int,input().split()))
    value.append(sum(now))
    board.append(now)
    #3r=r+sum -> 2r=sum
target=sum(value)//2
for ind in range(3):
    board[ind][ind]=target-value[ind]
for line in board:
    print(*line)
"""
0 1 6
3 0 7
4 9 0
"""