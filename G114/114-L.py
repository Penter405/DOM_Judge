"""
continuous range

"""
res=[]
for _ in range(int(input())):
    
    n=int(input())
    get=list(map(int,input().split()))
    #dp
    max_p=get[0]
    for rs in range(1,len(get)):
        get[rs]=max(get[rs],get[rs]+get[rs-1])#must choose yourself
        max_p=max(max_p,get[rs])
    if max_p<=0:
        res.append(0)
    else:
        res.append(max_p)

for rs in res:
    if rs>0:
        print(f"The maximum winning streak is {rs}.")
    else:
        print("Losing streak.")
    
