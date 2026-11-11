res=[]
for _ in range(int(input())):
    origin=int(input())
    d=origin
    status=0#-1  -> not  , 1 -> is
    appear=set([d])
    while True:
        buffer=0
        while d>0:
            buffer+=(d%10)*(d%10)
            d//=10
        d=buffer
        if d==1:
            status=1
            break
        if d in appear:
            status=-1
            break
        appear.add(d)
    if status==1:
        res.append(f"Case #{_+1}: {origin} is a Happy number.")
    else:
        res.append(f"Case #{_+1}: {origin} is an Unhappy number.")

for rs in res:
    print(rs)
    
    