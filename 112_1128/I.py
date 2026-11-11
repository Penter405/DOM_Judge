from sys import stdin
d=stdin.read().split("\n")[:-1]
out=[]
for line in d:
    new=[]
    for data in line:
        if data=="," or "0"<=data<="9":
            new.append(data)
    me="".join(new)
    me=me.split(",")
    res=0
    for rs in me:
        if rs=="":
            rs=0
        rs=int(rs)
        res+=rs
    out.append(res)

for rs in out:
    print(rs)
    