"""
2+2=2*2=4
3+3<3*3
4+4<4*4
5=2+3->6
2,3,4
12 - 4 4 4 -> 64
12 - 3 3 3 3 -> 81
"""
def get(a,b,out=10**9+7):
    if b==1:
        return a%out
    if b%2==0:
        return ((get(a,b//2,out)%out)*2)%out
    return (((get(a,b//2,out))%out)*((get(a,b//2+1,out))%out))%out


for _ in range(int(input())):
    d=int(input())
    res=1
    amount=d//3
    if d<=3:
        print(d)
        continue
    if d%3==1:
        amount-=1
        res=4
    elif d%3==2:
        res=2
    """
    for time in range(amount):
        res*=3
        if res>(10**9+7):
            res%=(10**9+7)6
    """
    res*=3**amount
    res%=(10**9+7)
    print(res)
