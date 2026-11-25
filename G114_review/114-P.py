for _ in range(int(input())):
    target=int(input())
    d=target
    res=0
    now=2
    while d!=1:
        if now>=int(target**0.5)+1:
            res+=d
            break
        while d%now==0:
            res+=now
            d//=now
        now+=1
    print(res)