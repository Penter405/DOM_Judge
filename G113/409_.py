def get(n):
    for a in range(int(n**0.5)+1):
        for b in range(a,int(n**0.5)+1):
            c2=n-a**2-b**2
            if c2<0:
                continue
            c=c2**0.5
            if c==int(c):
                return a,b,int(c)
    return -1
res=[]
for _ in range(int(input())):
    now=get(int(input()))
    if now==-1:
        res.append("-1")
    else:
        res.append(" ".join(list(map(str,now))))
for rs in res:
    print(rs)

