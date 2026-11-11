res=[]
while True:
    try:
        y,x=list(map(int,input().split(",")))
    except:
        break
    now=0
    board=[list(map(int,input().split(","))) for _ in range(y)]
    for n in range(1,min(y,x)+1):
        for sy in range(y-n+1):
            for sx in range(x-n+1):
                good=True
                for ny in range(n):
                    if not good:
                        break
                    for nx in range(n):
                        if board[sy+ny][sx+nx]==0:
                            good=False
                            break
                if good:
                    now+=1
    res.append(now)

for rs in res:
    print(rs)
