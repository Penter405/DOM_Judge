a=input()
b=input()
c=input()
la=len(a)
lb=len(b)
lc=len(c)
board=[[[0]*(lc+1) for _ in range(lb+1)] for _ in range(la+1)]
for y in range(1,la+1):
    for x in range(1,lb+1):
        for z in range(1,lc+1):
            if a[y-1]==b[x-1]==c[z-1]:
                board[y][x][z]=board[y-1][x-1][z-1]+1
            else:
                board[y][x][z]=max(board[y-1][x][z],board[y][x-1][z],board[y][x][z-1])
print(board[-1][-1][-1])