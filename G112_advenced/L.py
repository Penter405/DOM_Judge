res=[]
while True:
    d=int(input())
    if d==0:
        break
    while d//10!=0:
        buffer=0
        while d>0:
            buffer+=d%10
            d//=10
        d=buffer

    res.append(d)

    

for rs in res:
    print(rs)