memo=dict()
def mo(a,b,m):
    if b==1:
        return a%m
    if (a,b,m) in memo:
        return memo[(a,b,m)]
    
    if b&1:
        ans=((mo(a,b//2,m)%m)*mo(a,b//2+1,m)%m)%m
        memo[(a,b,m)]=ans
        return ans
    else:
        ans=mo(a,b//2,m)%m
        ans=(ans*ans)%m
        memo[(a,b,m)]=ans
        return ans

for _ in range(int(input())):
    a,b,m=list(map(int,input().split()))
    print(mo(a,b,m))