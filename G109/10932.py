n=int(input())
res=[]
for _ in range(n):
    d=list(map(int,input().split()))
    big=[0]*len(d)
    for rs in range(len(d)):
        if rs==0:
            big[rs]=max(0,d[rs])
        else:
            big[rs]=max(big[rs-1]+d[rs],0)
    want=max(big)
    if want==0:
        res.append(max(d))
    else:
        res.append(str(want))

for rs in res:
    print(rs)