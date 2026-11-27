"""
if %==same and //==same -> it is
"""
for _ in range(int(input())):
    a,b=list(map(int,input().split()))
    repeats=-1
    repeate=-1
    front=a//b
    a%=b
    res=[]
    past=dict()
    best=False
    ind=-1
    while True:
        ind+=1
        a*=10
        nowd=a//b
        nowl=a%b
        if (nowd,nowl) in past:
            repeats=past[(nowd,nowl)]
            repeate=ind
            break
        res.append(str(nowd))
        past[(nowd,nowl)]=ind
        a=nowl


    if repeate-repeats>50:
        print(f"{front}.{''.join(res[:repeats])}({''.join(res[repeats:repeats+50])}...)")
    else:
        print(f"{front}.{''.join(res[:repeats])}({''.join(res[repeats:repeate])})")