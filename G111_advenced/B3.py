res=[]
while True:
    try:
        d=list(map(float,input().split()))
    except:
        break
    address=list();appear=dict()
    bad=[]
    dam=None
    index=-1
    for rs in range(0,8,2):
        index+=1
        if (d[rs],d[rs+1]) in appear:
            bad=[rs,rs+1]
            dam=appear[(d[rs],d[rs+1])]
        address.append( [d[rs],d[rs+1]] )
        appear[(d[rs],d[rs+1])]=index
    address.pop(dam)
    res.append(    ( address[0][0] +address[2][0] -address[1][0]  ,  address[0][1] +address[2][1] -address[1][1] )   )


for a,b in res:
    if a!=int(a):
        a=str(a).split(".")
        a[1]=a[1][:3]
        a="".join(a)
    if b!=int(b):
            b=str(b).split(".")
            b[1]=b[1][:3]
            b="".join(b)
    print(a,b)