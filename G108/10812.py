from collections import defaultdict
"""
now= now get ball
X -> free next 2
/ -> free next 1
"""
def get():
    d=input().split()
    times=defaultdict(int)
    p1=0
    p2=1
    res=0
    gamed=0
    while p2<=len(d)-1:
        if gamed==10:
            break
        if d[p1]=="X":
            times[p1+1]+=1
            times[p1+2]+=1
            res+=10
            p1=p1+1
            p2=p1+1
        else:
            if d[p2]=="/":
                times[p2+1]+=1
                res+=10
            else:
                res+=int(d[p1])+int(d[p2])
            p1=p1+2
            p2=p1+1
        gamed+=1

    for rs in range(len(d)):
        if d[rs]=="X":
            now=10
        elif d[rs]=="/":
            now=10-int(d[rs-1])
        else:
            now=int(d[rs])
        res+=now*times[rs]
    return res
res=[]
for _ in range(int(input())):
    res.append(get())

for rs in res:
    print(rs)


"""

X X X X X X X X X X X X should be 300, which is exactly 2 extra ball
"""