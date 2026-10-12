res=[]

for _ in range(int(input())):
    d=int(input())
    me=[]
    for rs in range(9,1,-1):
        while d%rs==0:
            d=d//rs
            me.append(str(rs))

    if len(me)==0 or d!=1:
        res.append("-1")
    else:
        res.append("".join( me[::-1] ))


for rs in res:
    print(rs)
