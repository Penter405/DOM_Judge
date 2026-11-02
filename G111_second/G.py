res=[]
for _ in range(int(input())):
    a,b=input().split()
    a1=a.split(".")
    b1=b.split(".")
    d=str(int("".join(a1))*int("".join(b1))).zfill(len(a)-1+len(b)-1)
    floatsize=0
    if len(a1)==2:
        floatsize+=len(a1[1])
    if len(b1)==2:
        floatsize+=len(b1[1])
    if floatsize:
        res.append(str(int(d[:len(d)-floatsize]))+"."+d[len(d)-floatsize:])
    else:
        res.append(d)

print("\n".join(res))