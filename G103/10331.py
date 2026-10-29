from collections import Counter
res=[]


def cheak():
    ha=sorted(list(map(int,input().split())))
    d=[]
    for rs in ha:
        if rs%13==0:
            d.append(13)
        else:
            d.append(rs%13)
    co=Counter(d)
    me=dict(co)
    k=sorted(list(me.keys()).copy())
    inc=0
    last=None
    laflo=None
    for rs in sorted(list(set(ha))):
        if inc>=5:
            break
        if rs%13==1:
            hasa=rs+13
        if laflo!=None and laflo!=(rs-1)//13:
            inc=1
            laflo=(rs-1)//13
            continue
        laflo=(rs-1)//13
        if last==None or rs-1==last:
            inc+=1
        else:
            inc=1
        last=rs
    if inc>=5 or (inc>=4 and hasa!=False and last+1==hasa):
        return 7
    if 6>co.most_common(1)[0][1]>=4 and len(k)>=2:
        return 6
    v=sorted(list(me.values()))
    if len(v)>=2 and v[-2]>=2 and v[-1]>=3:
        return 5
    

    inc=0
    hasa=False
    last=None
    for rs in k:
        if inc >=5:
            break
        if rs%13==1:
            hasa=rs+13
        if last==None or rs-1==last:
            inc+=1
        else:
            inc=1
        last=rs
    if inc>=5 or (inc>=4 and hasa!=False and last+1==hasa):
        return 4
    if v[-1]>=3:
        return 3
    if len(v)>=2 and v[-1]>=2 and v[-2]>=2:
        return 2
    if v[-1]>=2:
        return 1
    return 0

    
for _ in range(int(input())):
    res.append(str(cheak()))

for rs in res:
    print(rs)
"""
2
3 44 4 6 7 5
19 12 1 32 45 25 

2
14 16 18 19 20 21
4 17 30 43 9 22

1
11 12 13 14 15 16

1
1 8 10 11 12 13
"""