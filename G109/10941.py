"""
0/1 bag

"""
res=[]
while True:
    try:
        d=input()
    except:
        break
    d=d.split()
    target=int(d[0])
    d=list(map(int,d[2:]))
    fetch=[1]+[0]*target
    best=0
    for rs in d:
        for ind in range(len(fetch)-1,rs-1,-1):
            #ind-rs ==-1 ind==rs-1
            if fetch[ind-rs]==1:
                fetch[ind]=1
                if ind>best:
                    best=ind
    res.append(str(best))



for rs in res:
    print(rs)