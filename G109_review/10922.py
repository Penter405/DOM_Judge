for _ in range(int(input())):
    d=int(input())
    res=[]
    for ind in range(9,1,-1):
        while d%ind==0:
            d//=ind
            res.append(str(ind))
    if d==1:
        print(''.join(res[::-1]))
    else:
        print(-1)
    