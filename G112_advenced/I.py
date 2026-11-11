res=[]
while True:
    d=list(map(int,input().split()))
    if d.count(0)==4:
        break
    nh,nm,ch,cm=d
    nm+=nh*60
    cm+=ch*60
    if nm==cm:
        res.append(0)
        continue
    if nm>cm:
        res.append(24*60-nm+cm)
    else:
        res.append(cm-nm)

for rs in res:
    print(rs)

"""
1 5 3 5
23 59 0 34
21 33 21 10
23 59 23 59
0 0 0 1
0 0 0 0

"""