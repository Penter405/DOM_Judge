"""
now= now get ball
X -> free next 2
/ -> free next 1
"""
def get():
    d=input().split()

    res=[0]
    times=[[0,0] for _ in range(10)]
    sub=0
    p1=0
    p2=1
    gamed=0
    while gamed<10:
        #print(d[p1],d[p2],p1,p2)
        if d[p1]=="X":
            res.append(10)
            if gamed+1<10:
                times[gamed+1][0]+=1
            if gamed+1<10:
                times[gamed+1][1]+=1
            p1+=1
            p2=p1+1
            sub+= times[gamed][0]*10
            if gamed==9:
                if d[p1]=="X":
                    sub+=10
                else:
                    if d[p2]=="/":
                        sub+=10
                    else:
                        sub+=int(d[p1])+int(d[p2])
        else:
            if d[p2]=="/":
                res.append(10)
                if gamed+1<10:
                    times[gamed+1][0]+=1
            else:
                res.append(int(d[p1])+int(d[p2]))
            sub+=times[gamed][0]*int(d[p1])
            
            if d[p2]=="/":
                b=10-int(d[p1])
            else:
                b=int(d[p2])
            sub+=times[gamed][1]*int(b)
            p1=p2+1
            p2=p1+1
        gamed+=1

    return (sum(res)+sub)

res=[]
for _ in range(int(input())):
    res.append(get())

for rs in res:
    print(rs)


"""

X X X X X X X X X X X X should be 300, which is exactly 2 extra ball
"""