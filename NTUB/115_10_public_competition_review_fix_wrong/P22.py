rule=[]
for _ in range(int(input())):
    status,which,port=input().split()
    port=int(port)
    rule.append([which,port,status])

   

res=[]
for _ in range(int(input())):
    which,port=input().split()
    port=int(port)
    for w,p,s in rule:
        if w=="ANY" or w==which:
            if p==-1 or p==port:
                res.append(s)
                break
    else:
        res.append("DENY")

for rs in res:
    print(rs)
    