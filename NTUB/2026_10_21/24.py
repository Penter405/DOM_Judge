k=int(input())
d=input()

while ever:
    ever=False
    new=[]
    

last=None
def formating(data):
    res=[]
    for rs in data:
        if last==None or last!=rs:
            res.append([])
        res[-1].append(rs)
        last=rs
    return res

def disfor(data):
    res=[]
    for rs in data:
        if len(rs)>0:
            res.append("".join(rs))
    return res
def translate(data):
    global ever
    res=[]
    for rs in data:
        if len(rs)>=3:
            ever=True
            if len(rs)%3==0:
                continue
            res.append(rs[0]*(len(rs)%3))

while ever:
    ever=False
    d=formating(d)
    d=translate(d)

d=disfor(d)
    

if len(d)==0:
    print("EMPTY")
else:
    print(d)
"""
aabbbbbbbbbbba

"""