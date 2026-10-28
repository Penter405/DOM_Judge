"""
res=[]
for _ in range(int(input())):
    a,b=list(map(int,input().split()))
    res.append((f"{a/b:.55f}"))
    if (a/b)*(10**50)==(a/b)*(10**50)//1:
        print(f"{a/b}(0)")

    d=f"{a/b:.55f}".split(".")[1]
    for rs in range(len("{a/b:.60f}")):
        if d.count(d[:rs+1])>=(60-rs+1)//rs+1:
            res.append(f"{(a/b)//1}.({d[:rs+1]})")
    res.append((f"{(a/b//1)}.({d[:51]}...)"))

        
"""
res=[]
def int_list_to_str(n):
    return "".join(list(map(str,n)))


def cheak():
    a,b=list(map(int,input().split()))
    d=[];appeared=dict()# (devi,left)  : place (0 indexed)
    d.append(str(a//b))
    d.append([])
    a%=b
    seeing=-1
    while True:
        seeing+=1
        a*=10
        now_devision=a//b
        now_left=a%b
        a%=b
        if now_left==0:
            if (now_devision)==0:
                return d[0]+"."+int_list_to_str(d[1])+"(0)"
            return d[0]+"."+int_list_to_str(d[1])+str(now_devision)+"(0)"
        if (now_devision,now_left) in appeared:
            return (d,appeared[(now_devision,now_left)],seeing-1)
        appeared[(now_devision,now_left)]=seeing
        d[-1].append(now_devision)

for _ in range(int(input())):
    d=cheak()
    if type(d)==str:
        res.append(d)
        continue
    devisioned,first_place,last_place=d
    if len(devisioned[1])>50:
        now=devisioned[0]+"."+int_list_to_str(devisioned[1][:first_place])+"("+int_list_to_str(devisioned[1][first_place:min(50,last_place+1)])+"...)"
    else:
        now=devisioned[0]+"."+int_list_to_str(devisioned[1][:first_place])+"("+int_list_to_str(devisioned[1][first_place:last_place+1])+")"
    res.append(now)


print("\n".join(res))