out=[]
for _ in range(int(input())):
    res=[]
    n,want=list(map(int,input().split()))
    while n>0:
        got=n%want
        if got>=10:
            got=chr(65+got-10)
        else:
            got=str(got)
        res.append(got)
        n//=want
    if len(res)==0:
        res.append("0")
    out.append("".join(res[::-1]))
print("\n".join(out))