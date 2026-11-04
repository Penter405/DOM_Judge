def search(d,target):#find first bigger than me
    left=0
    right=len(d)-1
    while left<=right:
        mid=(left+right)//2
        if d[mid]>target:
            right=mid-1
        else:
            left=mid+1
    return left

"""
00:01
hh:mm
-> h.front0.erase
0:01
if hh=0 -> only cheak integer of mm

"""
good=[]
for h in range(24):
    for m in range(60):
        if h==0:
            if str(m)==str(m)[::-1]:
                good.append("00"+":"+str(m).zfill(2))
        else:
            bot=str(h)+str(m).zfill(2)
            if bot==bot[::-1]:
                good.append(str(h).zfill(2)+":"+str(m).zfill(2))
res=[]
for _ in range(int(input())):
    want=input()
    place=search(good,want)
    if place==len(good):
        res.append(good[0])
    else:
        res.append(good[place])

for rs in res:
    print(rs)
