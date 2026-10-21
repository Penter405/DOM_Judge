m,n,p=list(map(int,input().split()))

def cheak():
    a=3*n-2*p-m
    if a!=a//1:
        return False
    if a<0:
        return False
    b=-6*n+4*p+3*m
    if b<0:
        return False
    c=-p+2*n-m
    if c<0:
        return False
    return True


if cheak():
    print("YES")
else:
    print("NO")
