for _ in range(int(input())):
    a,b,n=list(map(int,input().split()))
    res=0
    for t in range(a,b+1):
        if str(n) in str(t):
            res+=1
    print(res)