res=[]
for _ in range(int(input())):
    a,b,c=list(map(int,input().split()))
    r=0
    for rs in range(a,b+1):
        if str(c) in str(rs):
            r+=1
    res.append(str(r))

print("\n".join(res))