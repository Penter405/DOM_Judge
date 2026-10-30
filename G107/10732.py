memo=dict()
def mod(a,b,x):
    if b==1:
        return a%x
    if (a,b,x) in memo:
        return memo[(a,b,x)]
    if b%2==0:
        me= (mod(a,b//2,x)**2)%x
    else:
        me=(mod(a,b//2,x)%x)*(mod(a,b//2+1,x)%x)%x
    memo[(a,b,x)]=me
    return me

res=[]
for _ in range(int(input())):
    a1,a2,b1,b2,c1,c2=list(map(int,input().split()))
    me=0
    for a in range(a1,a2+1):
        for b in range(b1,b2+1):
            for c in range(c1,c2+1):
                if (a+b)%c ==(a-b)%c:
                    me+=1
    res.append(str(me))

for rs in res:
    print(rs)