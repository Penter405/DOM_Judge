memo=dict()
def get(b,p,m):
    if (b,p,m) in memo:
        return memo[(b,p,m)]
    if p<=1:
        return (b**p)%m
    if p%2==0:
        ans=get(b,p//2,m)*get(b,p//2,m)%m
    else:
        ans=get(b,1,m)*get(b,p//2,m)*get(b,p//2,m)%m
    memo[(b,p,m)]=ans
    return ans
res=[]
did=-1
while True:
    did+=1
    try:
        if did!=0:
            u=input()
        b=int(input())
        p=int(input())
        m=int(input())
    except:
        break
    res.append(str(get(b,p,m)))

print("\n".join(res))