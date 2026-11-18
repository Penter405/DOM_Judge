#DNF, this is try again version

"""
21 * 21 * amount of board (10,000)
-> 4,000,000  10**6 *4
"""
def cheak(y,x,current):
    now=1
    left=x-1
    right=x+1
    top=y-1
    down=y+1
    while left>=0 and right<len(board[0]) and top>=0 and down<len(board):
        #ever not legal -> return now
        for x in range(left,right+1):
            if board[top][x]!=current or board[down][x]!=current:
                return now
        for y in range(top,down+1):
            if board[y][left]!=current or board[y][right]!=current:
                return now
        left-=1
        right+=1
        top-=1
        down+=1
        now+=2
    return now
for _ in range(int(input())):
    by,bx,ask=list(map(int,input().split()))
    print(by,bx,ask)
    board=[]
    for _ in range(by):
        board.append(input())
    for _ in range(ask):
        sy,sx=list(map(int,input().split()))
        print(cheak(sy,sx,board[sy][sx]))
"""
1
7 10 4
abbbaaaaaa
abbbaaaaaa
abbbaaaaaa
aaaaaaaaaa
aaaaaaaaaa
aaccaaaaaa
aaccaaaaaa
1 2
2 4
4 6
5 2
"""