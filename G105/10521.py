res=[]
for _ in range(int(input())):
    a,b=input().split("/")
    a=a.split(".")
    b=b.split(".")
    r=[]
    for rs in range(4):
        r.append(str(int(a[rs])&int(b[rs])))

    res.append(".".join(r))

for rs in res:
    print(rs)