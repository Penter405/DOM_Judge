#math?
res=[]
for _ in range(int(input())):
    a,b=list(map(int,input().split()))
    now=int(a**0.5)
    if now**2!=a:
        now+=1
    now2=int(b**0.5)
    res.append(now2-now+1)
for rs in res:
    print(rs)