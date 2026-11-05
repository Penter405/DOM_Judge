def far(a,b):
    if b==a:
        return 0
    if b<a:
        return ord(a)-ord(b)

    return ord(b)-ord(a)
res=[]
d=input()
for rs in range(len(d)-1):
    res.append(str(far(d[rs],d[rs+1])))
print("".join(res))