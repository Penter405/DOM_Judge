y1,x1,y2,x2=list(map(int,input().split()))
"""
for a 
    for b
"""

board=[[-1]*(x1*x2) for _ in range(y1*y2)]
a=[]
for _ in range(y1):
    a.append(list(map(int,input().split())))

b=[]
for _ in range(y2):
    b.append(list(map(int,input().split())))

#double for a
for ya in range(y1):
    for xa in range(x1):
        #double for b

        for yb in range(y2):
            for xb in range(x2):
                yn=ya*y2+yb
                xn=xa*x2+xb
                board[yn][xn]=a[ya][xa]*b[yb][xb]
for line in board:
    print(*line)
