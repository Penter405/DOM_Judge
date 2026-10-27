
def mod(x,y,m):
    if y==1:
        return x%m
    if y%2==0:
        return ((mod(x,y//2,m)%m)**2)%m

    return ((mod(x,y//2,m)%m)*(mod(x,y//2+1,m)%m))%m
res=[]
for _ in range(int(input())):
    x,y,m=list(map(int,input().split()))
    res.append(str(mod(x,y,m)))
#a*b mod c=a mod c * b mod c
print("\n".join(res))

