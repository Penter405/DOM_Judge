d=int(input())
res=[]
me=1
while d!=1:
    me+=1
    count=0
    while d%me==0:
        count+=1
        d//=me
    if count!=0:
        if count==1:
            res.append(str(me))
        else:
            res.append(str(me)+"^"+str(count))
print(" * ".join(res))