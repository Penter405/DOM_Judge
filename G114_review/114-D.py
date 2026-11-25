for _ in range(int(input())):
    a,b=list(map(int,input().split()))
    if a%2==0:
        a+=1
    if b%2==0:
        b-=1
    res=0
    for tar in range(a,b+1,2):
        res+=tar
    print(res)