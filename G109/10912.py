def get():
    d=input()
    out=[];fri=[]
    ever1=False
    for rs in d:
        if rs=="4":
            out.append("3")
            fri.append("1")
            ever1=True
        else:
            out.append(rs)
            if ever1:
                fri.append("0")
    return "".join(out)+" "+"".join(fri)

res=[]
for _ in range(int(input())):
    res.append(get())


for rs in res:
    print(rs)
