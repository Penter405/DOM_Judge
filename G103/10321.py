res=[]
for _ in range(int(input())):
    a=input()
    b=input()
    now=list(set(a)&set(b))
    if len(now)==0:
        res.append("N")
    else:
        now.sort()
        res.append("".join(now))


for rs in res:
    print(rs)