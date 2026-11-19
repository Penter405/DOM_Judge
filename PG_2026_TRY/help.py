memo={}
def get(a,b,out=10**9+7):
    if (a,b) in memo:
        return memo[(a,b)]
    if b==1:
        good=a%out
    elif b%2==0:
        good= ((get(a,b//2,out)%out)*2)%out
    else:
        good=(((get(a,b//2,out))%out)*((get(a,b//2+1,out))%out))%out
    memo[(a,b)]=good
    return good
print(get(10,20000,9)) 