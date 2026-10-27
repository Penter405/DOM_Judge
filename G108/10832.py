res=[]
for _ in range(int(input())):
    a,b=list(map(int,input().split()))
    res.append((f"{a/b:.55f}"))
    if (a/b)*(10**50)==(a/b)*(10**50)//1:
        print(f"{a/b}(0)")

    d=f"{a/b:.55f}".split(".")[1]
    for rs in range(len("{a/b:.60f}")):
        if d.count(d[:rs+1])>=(60-rs+1)//rs+1:
            res.append(f"{(a/b)//1}.({d[:rs+1]})")
    res.append((f"{(a/b//1)}.({d[:51]}...)"))

        
