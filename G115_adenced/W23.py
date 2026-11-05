def imnot(d):
    res=[]
    for rs in d:
        if rs=="1":
            res.append("0")
        else:
            res.append("1")
    return "".join(res)


res=[]
for _ in range(int(input())):
    me,friend=input().split("/")
    me=me.split(".")
    friend=friend.split(".")
    hi=[]
    damn=[]

    for rs in range(4):
        hi.append(str(int(me[rs]) & int(friend[rs])))
        #me and friend -> hi
        #me or (not friend)  ->damn
    for rs in range(4):
        a=int(me[rs])
        b=int(imnot((bin(int(friend[rs]))[2:]).zfill(8)),2)
        damn.append(str(a | b))
    res.append(str(".".join(hi))+"/"+str(".".join(damn)))

print("\n".join(res))