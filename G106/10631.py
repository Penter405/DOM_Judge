def rever(n):
    n=n.zfill(8)
    res=[]
    for rs in n:
        if rs==".":
            res.append(".")
            continue

        if rs=="1":
            res.append("0")
        else:
            res.append("1")
    return "".join(res)
def ever(a,b):
    res=[]
    a=a.zfill(8)
    b=b.zfill(8)
    for rs in range(len(a)):
        if a[rs]=="1" or b[rs]=="1":
            res.append("1")
        else:
            res.append("0")
    return "".join(res)
res=[]
for _ in range(int(input())):
    ip, child =input().split("/")
    ip=list(map(int,ip.split(".")))
    child=list(map(int,child.split(".")))
    a=[]
    for rs in range(4):
        a.append(str(int(ever(bin(ip[rs])[2:],rever(bin(child[rs])[2:])),2)))

    res.append(".".join(a))

for rs in res:
    print(rs)

"""
5
139.175.153.252/255.255.0.0
10.104.69.0/255.255.255.192
192.15.156.205/255.255.255.224
192.168.10.65/255.255.255.224
10.240.168.19/255.255.192.0 
"""